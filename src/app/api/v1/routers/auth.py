from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from ....models.auth import (
    UserSignUp, 
    UserLogin, 
    UserResponse, 
    LoginResponse,
    HTTPError
)
from ....services.auth import auth_service
from typing import Dict

router = APIRouter(tags=["auth"])

# Update the tokenUrl to match our actual login endpoint
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",  # Updated to match the full path
    scheme_name="JWT"
)
security = HTTPBearer()

@router.post("/signup", 
    response_model=UserResponse,
    summary="Sign up a new user",
    description="Create a new user account with email and password"
)
async def sign_up(user_data: UserSignUp) -> UserResponse:
    """
    Sign up a new user.
    
    Parameters:
    - **email**: Valid email address
    - **password**: Password (minimum 8 characters)
    - **full_name**: User's full name
    
    Returns:
    - User profile information
    """
    try:
        return await auth_service.sign_up(user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login",
    response_model=LoginResponse,
    summary="Log in a user",
    description="Login with email and password to get access token",
    responses={
        200: {
            "description": "Successful login",
            "model": LoginResponse
        },
        401: {
            "description": "Invalid credentials",
            "model": HTTPError
        },
        422: {
            "description": "Validation Error",
            "model": HTTPError
        }
    }
)
async def login(credentials: UserLogin) -> LoginResponse:
    """
    Log in a user.
    
    Parameters:
    - **email**: Registered email address
    - **password**: User password
    
    Returns:
    - Access token and user information
    """
    try:
        return await auth_service.login(credentials)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/logout",
    response_model=Dict[str, str],
    summary="Log out current user",
    description="Log out the currently authenticated user",
    responses={
        200: {
            "description": "Successfully logged out",
            "content": {
                "application/json": {
                    "example": {"message": "Successfully logged out"}
                }
            }
        },
        401: {
            "description": "Invalid or expired token",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid authentication credentials"}
                }
            }
        }
    }
)
async def logout(credentials: HTTPAuthorizationCredentials = Security(security)) -> Dict[str, str]:
    """
    Log out the current user.
    
    Requires:
    - Bearer token authentication
    
    Returns:
    - Success message
    """
    try:
        # The token is automatically added to the Supabase client's session
        await auth_service.logout(credentials.credentials)
        return {"message": "Successfully logged out"}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e)) 