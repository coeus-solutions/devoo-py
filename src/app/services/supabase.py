from supabase import create_client, Client
from ..core.config import get_settings

settings = get_settings()

def get_supabase_client() -> Client:
    """Initialize and return regular Supabase client."""
    return create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_KEY
    )

def get_service_role_client() -> Client:
    """Initialize and return Supabase client with service role key."""
    return create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_SERVICE_ROLE_KEY
    )

# Initialize both clients
supabase = get_supabase_client()
service_role_client = get_service_role_client()

# Export all necessary functions and instances
__all__ = ['supabase', 'service_role_client', 'get_supabase_client', 'get_service_role_client'] 