from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any, Union

class ValidationErrorDetail(BaseModel):
    loc: List[str] = Field(..., description="Location of the error")
    msg: str = Field(..., description="Error message")
    type: str = Field(..., description="Error type")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "loc": ["body", "field_name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        }
    )

class HTTPError(BaseModel):
    detail: str = Field(..., description="Error detail message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "detail": "Error message here"
            }
        }
    )

class HTTPValidationError(BaseModel):
    detail: List[ValidationErrorDetail] = Field(..., description="List of validation errors")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "detail": [
                    {
                        "loc": ["body", "field_name"],
                        "msg": "field required",
                        "type": "value_error.missing"
                    }
                ]
            }
        }
    )

# Export all models
__all__ = ['HTTPError', 'HTTPValidationError', 'ValidationErrorDetail'] 