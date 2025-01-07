from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class UserSignUp(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    full_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    avatar_url: Optional[str] = None

class UserProfileResponse(BaseModel):
    id: str
    email: str
    full_name: str
    avatar_url: Optional[str] = None

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserProfileResponse

# Add the HTTPError model
class HTTPError(BaseModel):
    detail: str 