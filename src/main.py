import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.api.v1.router import router as v1_router
from app.core.config import debug_env
from app.models.auth import UserLogin, LoginResponse, UserResponse, UserProfileResponse
from app.models.schemas import ProjectStatus, ProjectCreate, ProjectResponse
from app.models.responses import HTTPError, HTTPValidationError, ValidationErrorDetail
from app.models.chat import MessageCreate, MessageResponse, ConversationCreate, ConversationResponse

app = FastAPI(
    title="Devoo API",
    description="AI-powered software development assistant",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "auth",
            "description": "Authentication operations"
        },
        {
            "name": "projects",
            "description": "Project management operations"
        },
        {
            "name": "chat",
            "description": "Chat operations"
        }
    ]
)

# Define custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Devoo API",
        version="1.0.0",
        description="AI-powered software development assistant",
        routes=app.routes,
    )
    
    # Add security scheme and components
    openapi_schema["components"] = {
        "securitySchemes": {
            "Bearer": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
                "description": "Enter the token you received from the login endpoint"
            }
        },
        "schemas": {}
    }

    # Add model schemas
    schemas = openapi_schema["components"]["schemas"]
    
    # Add validation error detail schema
    validation_error_schema = ValidationErrorDetail.model_json_schema()
    schemas["ValidationErrorDetail"] = validation_error_schema
    
    # Add HTTP error schema
    http_error_schema = HTTPError.model_json_schema()
    schemas["HTTPError"] = http_error_schema
    
    # Add HTTP validation error schema
    validation_error_schema = HTTPValidationError.model_json_schema()
    schemas["HTTPValidationError"] = validation_error_schema
    
    # Auth models
    schemas["UserLogin"] = UserLogin.model_json_schema()
    schemas["UserProfileResponse"] = UserProfileResponse.model_json_schema()
    schemas["LoginResponse"] = LoginResponse.model_json_schema()
    
    # Project models
    schemas["ProjectCreate"] = ProjectCreate.model_json_schema()
    schemas["ProjectResponse"] = ProjectResponse.model_json_schema()
    schemas["ProjectStatus"] = ProjectStatus.model_json_schema()
    
    # Chat models
    schemas["MessageCreate"] = MessageCreate.model_json_schema()
    schemas["MessageResponse"] = MessageResponse.model_json_schema()
    schemas["ConversationCreate"] = ConversationCreate.model_json_schema()
    schemas["ConversationResponse"] = ConversationResponse.model_json_schema()
    
    # Add global security requirement
    openapi_schema["security"] = [{"Bearer": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Set custom OpenAPI schema
app.openapi = custom_openapi

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(v1_router, prefix="/api/v1")

if __name__ == "__main__":
    print("\n=== Environment Configuration ===")
    debug_env()
    print("\n=== Starting Server ===")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 