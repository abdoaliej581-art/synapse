"""Custom exceptions for S.Y.N.A.P.S.E."""


class SynapseError(Exception):
    """Base exception for all S.Y.N.A.P.S.E errors."""


class ConfigurationError(SynapseError):
    """Raised when there is a configuration problem."""


class AgentError(SynapseError):
    """Raised when an agent encounters an error."""


class MemoryError(SynapseError):
    """Raised when the memory system encounters an error."""


class PerceptionError(SynapseError):
    """Raised when the perception layer encounters an error."""


class SimulationError(SynapseError):
    """Raised when simulation fails."""
