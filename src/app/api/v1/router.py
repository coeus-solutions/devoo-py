from fastapi import APIRouter
from .routers import projects, auth, chat
from ...core.config import get_settings

router = APIRouter()

router.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)

router.include_router(
    projects.router,
    prefix="/projects",
    tags=["projects"]
)

router.include_router(
    chat.router,
    prefix="/chat",
    tags=["chat"]
)

@router.get("/")
async def root():
    return {"message": "Welcome to Devoo API v1"}

@router.get("/debug/settings")
async def debug_settings():
    """Debug endpoint to verify environment variables (DISABLE IN PRODUCTION)"""
    settings = get_settings()
    return {
        "supabase_url": settings.SUPABASE_URL,
        # Don't return sensitive keys in production!
        "has_supabase_key": bool(settings.SUPABASE_KEY),
        "has_service_role_key": bool(settings.SUPABASE_SERVICE_ROLE_KEY),
        "has_jwt_token": bool(settings.SUPABASE_JWT_TOKEN),
        "has_anthropic_key": bool(settings.ANTHROPIC_API_KEY),
        "has_perplexity_key": bool(settings.PERPLEXITY_API_KEY),
    } 