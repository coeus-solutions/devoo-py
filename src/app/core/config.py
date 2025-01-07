from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path
import os

# Get the absolute path to the root directory (where .env is located)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENV_FILE = os.path.join(ROOT_DIR, '.env')

class Settings(BaseSettings):
    # Supabase settings
    SUPABASE_URL: str
    SUPABASE_KEY: str  # This is the anon key
    SUPABASE_SERVICE_ROLE_KEY: str
    SUPABASE_JWT_TOKEN: str
    
    # AI API settings
    ANTHROPIC_API_KEY: str
    PERPLEXITY_API_KEY: str
    
    class Config:
        env_file = ENV_FILE
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Get settings with explicit .env file path."""
    if not os.path.exists(ENV_FILE):
        raise FileNotFoundError(f"Environment file not found at: {ENV_FILE}")
    return Settings(_env_file=ENV_FILE)

# Add this for debugging
def debug_env():
    """Debug function to check environment loading"""
    print(f"Looking for .env at: {ENV_FILE}")
    print(f"File exists: {os.path.exists(ENV_FILE)}")
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r') as f:
            print("Environment file contents:")
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key = line.split('=')[0]
                    print(f"{key}: {'✓' if os.getenv(key) else '✗'}") 