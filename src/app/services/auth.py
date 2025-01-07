from typing import Dict, Any
from ..models.auth import UserSignUp, UserLogin, LoginResponse, UserProfileResponse
from .supabase import supabase, service_role_client
from fastapi import HTTPException
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self):
        self.supabase = supabase
        self.service_role_client = service_role_client
    
    async def sign_up(self, user_data: UserSignUp) -> Dict[str, Any]:
        """Sign up a new user."""
        try:
            # Create auth user with regular client
            auth_response = self.supabase.auth.sign_up({
                "email": user_data.email,
                "password": user_data.password,
                "options": {
                    "data": {
                        "full_name": user_data.full_name
                    }
                }
            })
            
            logger.info(f"Auth response: {auth_response}")
            
            if not auth_response.user:
                raise HTTPException(status_code=400, detail="Failed to create user")
            
            # Create user profile with service role client to bypass RLS
            profile_data = {
                "id": auth_response.user.id,
                "full_name": user_data.full_name,
                "avatar_url": None
            }
            
            # Insert into user_profiles table using service role client
            profile_result = self.service_role_client.table("user_profiles").insert(profile_data).execute()
            logger.info(f"Profile creation result: {profile_result}")
            
            if not profile_result.data:
                raise HTTPException(status_code=400, detail="Failed to create user profile")
            
            return {
                "id": auth_response.user.id,
                "email": auth_response.user.email,
                "full_name": user_data.full_name,
                "avatar_url": None
            }
        except Exception as e:
            logger.error(f"Sign up error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))

    async def login(self, credentials: UserLogin) -> LoginResponse:
        """Log in a user."""
        try:
            logger.info(f"Attempting login for email: {credentials.email}")
            
            # Try to sign in
            auth_response = self.supabase.auth.sign_in_with_password({
                "email": credentials.email,
                "password": credentials.password
            })
            
            logger.info(f"Auth response received: {auth_response}")
            
            if not auth_response.user:
                logger.error("No user in auth response")
                raise HTTPException(status_code=401, detail="Invalid credentials")
            
            # Get user profile using service role client to ensure access
            try:
                profile = self.service_role_client.table("user_profiles") \
                    .select("*") \
                    .eq("id", auth_response.user.id) \
                    .single() \
                    .execute()
                
                logger.info(f"Profile retrieved: {profile}")
                
                if not profile.data:
                    logger.error(f"No profile found for user {auth_response.user.id}")
                    raise HTTPException(status_code=404, detail="User profile not found")
                
                # Create response matching LoginResponse model
                return LoginResponse(
                    access_token=auth_response.session.access_token,
                    token_type="bearer",
                    user=UserProfileResponse(
                        id=auth_response.user.id,
                        email=auth_response.user.email,
                        full_name=profile.data["full_name"],
                        avatar_url=profile.data.get("avatar_url")
                    )
                )
            except Exception as profile_error:
                logger.error(f"Error retrieving profile: {str(profile_error)}")
                raise HTTPException(status_code=500, detail="Error retrieving user profile")
                
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")

    async def logout(self, token: str) -> None:
        """Log out a user using their token."""
        try:
            logger.info("Attempting to logout user")
            # For Supabase, we don't need to pass the token to sign_out
            self.supabase.auth.sign_out()
            logger.info("Successfully logged out user")
        except Exception as e:
            logger.error(f"Logout error: {str(e)}")
            raise HTTPException(status_code=401, detail="Failed to logout")

auth_service = AuthService() 