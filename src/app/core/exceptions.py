class DevooError(Exception):
    """Base exception for Devoo application."""
    pass

class AIGenerationError(DevooError):
    """Raised when there's an error in AI generation."""
    pass

class DatabaseError(DevooError):
    """Raised when there's a database error."""
    pass

class AuthenticationError(DevooError):
    """Raised when there's an authentication error."""
    pass 