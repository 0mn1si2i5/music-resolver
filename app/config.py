import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the module root (parent of app/)
_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_ENV_PATH)


class Settings:
    FASTAPI_HOST: str = os.environ.get("FASTAPI_HOST", "127.0.0.1")
    FASTAPI_PORT: int = int(os.environ.get("FASTAPI_PORT", "8788"))
    CORS_ORIGINS: str = os.environ.get("CORS_ORIGINS", "")

    # Spotify API credentials
    SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", "")
    SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", "")

    # Netease Cloud Music API
    NETEASE_API_BASE_URL: str = os.environ.get("NETEASE_API_BASE_URL", "http://localhost:3000")
    NETEASE_REQUEST_TIMEOUT: int = int(os.environ.get("NETEASE_REQUEST_TIMEOUT", "10"))

    # Apple Music
    APPLE_MUSIC_STOREFRONT: str = os.environ.get("APPLE_MUSIC_STOREFRONT", "cn")

    # Songlink API
    SONGLINK_API_KEY: str = os.environ.get("SONGLINK_API_KEY", "")

    # Debug mode
    DEBUG: bool = os.environ.get("DEBUG", "false").lower() == "true"


settings = Settings()
