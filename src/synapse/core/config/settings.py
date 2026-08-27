"""Configuration management for S.Y.N.A.P.S.E."""

from pathlib import Path
from typing import Self

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_prefix="SYNAPSE_",
        extra="ignore",
    )

    # Application
    app_name: str = Field(default="S.Y.N.A.P.S.E", description="Application name")
    app_version: str = Field(default="0.1.0", description="Application version")
    debug: bool = Field(default=False, description="Enable debug mode")
    log_level: str = Field(default="INFO", description="Logging level")

    # Paths
    base_dir: Path = Field(
        default=Path(__file__).parent.parent.parent.parent,
        description="Base directory of the project",
    )

    @property
    def data_dir(self) -> Path:
        """Return the data directory path."""
        return self.base_dir / "data"

    @property
    def logs_dir(self) -> Path:
        """Return the logs directory path."""
        return self.data_dir / "logs"

    @property
    def models_dir(self) -> Path:
        """Return the models directory path."""
        return self.data_dir / "models"

    def ensure_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        for directory in [self.data_dir, self.logs_dir, self.models_dir]:
            directory.mkdir(parents=True, exist_ok=True)

    @classmethod
    def create_test_settings(cls) -> Self:
        """Create settings suitable for testing."""
        return cls(debug=True, log_level="DEBUG")


_settings: Settings | None = None


def get_settings() -> Settings:
    """Get cached application settings."""
    global _settings
    if _settings is None:
        _settings = Settings()
        _settings.ensure_directories()
    return _settings


def reset_settings() -> None:
    """Reset cached settings (useful for testing)."""
    global _settings
    _settings = None
