"""Unit tests for configuration settings."""

from collections.abc import Iterator
from pathlib import Path

import pytest

from synapse.core.config.settings import Settings, get_settings, reset_settings


@pytest.fixture(autouse=True)
def clean_settings() -> Iterator[None]:
    """Reset settings before each test."""
    reset_settings()
    yield
    reset_settings()


class TestSettings:
    """Test suite for Settings class."""

    def test_default_values(self) -> None:
        """Test that default values are set correctly."""
        settings = Settings()
        assert settings.app_name == "S.Y.N.A.P.S.E"
        assert settings.app_version == "0.1.0"
        assert settings.debug is False
        assert settings.log_level == "INFO"

    def test_data_dir_property(self) -> None:
        """Test data_dir property returns correct path."""
        settings = Settings()
        assert settings.data_dir == settings.base_dir / "data"

    def test_logs_dir_property(self) -> None:
        """Test logs_dir property returns correct path."""
        settings = Settings()
        assert settings.logs_dir == settings.data_dir / "logs"

    def test_models_dir_property(self) -> None:
        """Test models_dir property returns correct path."""
        settings = Settings()
        assert settings.models_dir == settings.data_dir / "models"

    def test_ensure_directories_creates_paths(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test that ensure_directories creates required directories."""
        settings = Settings(base_dir=tmp_path)
        settings.ensure_directories()

        assert (tmp_path / "data").exists()
        assert (tmp_path / "data" / "logs").exists()
        assert (tmp_path / "data" / "models").exists()

    def test_get_settings_caches_instance(self) -> None:
        """Test that get_settings returns the same instance."""
        settings1 = get_settings()
        settings2 = get_settings()
        assert settings1 is settings2

    def test_reset_settings_clears_cache(self) -> None:
        """Test that reset_settings clears the cached instance."""
        settings1 = get_settings()
        reset_settings()
        settings2 = get_settings()
        assert settings1 is not settings2

    def test_create_test_settings(self) -> None:
        """Test factory method for test settings."""
        settings = Settings.create_test_settings()
        assert settings.debug is True
        assert settings.log_level == "DEBUG"
