from enum import Enum
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, UUID4, Field
from datetime import datetime

class AgentStatus(str, Enum):
    QUEUED = "queued"
    ANALYZING = "analyzing"
    DESIGNING = "designing"
    IMPLEMENTING = "implementing"
    REVIEWING = "reviewing"
    COMPLETED = "completed"
    ERROR = "error"

class ProjectCreate(BaseModel):
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    requirements: str = Field(..., description="Project requirements")
    settings: Dict[str, Any] = Field(default_factory=dict, description="Project settings")

    class Config:
        schema_extra = {
            "example": {
                "name": "My Project",
                "description": "A sample project",
                "requirements": "Build a chat application",
                "settings": {}
            }
        }

class ProjectResponse(BaseModel):
    id: UUID4 = Field(..., description="Project ID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    status: str = Field(..., description="Project status")
    stackblitz_id: Optional[str] = Field(None, description="StackBlitz project ID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    class Config:
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "My Project",
                "description": "A sample project",
                "status": "initialized",
                "stackblitz_id": None,
                "created_at": "2024-03-20T12:00:00Z",
                "updated_at": "2024-03-20T12:00:00Z"
            }
        }

class AgentProgressUpdate(BaseModel):
    agent_type: str = Field(..., description="Type of agent")
    status: AgentStatus = Field(..., description="Current agent status")
    message: str = Field(..., description="Progress message")
    progress: float = Field(..., description="Progress percentage", ge=0, le=1)
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    class Config:
        schema_extra = {
            "example": {
                "agent_type": "requirements",
                "status": "analyzing",
                "message": "Analyzing project requirements",
                "progress": 0.5,
                "metadata": {}
            }
        }

class ProjectStatus(BaseModel):
    current_agent: str = Field(..., description="Currently active agent")
    overall_progress: float = Field(..., description="Overall project progress", ge=0, le=1)
    stage_progress: float = Field(..., description="Current stage progress", ge=0, le=1)
    status_message: str = Field(..., description="Current status message")
    last_update: datetime = Field(..., description="Last status update timestamp")

    class Config:
        schema_extra = {
            "example": {
                "current_agent": "requirements",
                "overall_progress": 0.25,
                "stage_progress": 0.5,
                "status_message": "Analyzing requirements",
                "last_update": "2024-03-20T12:00:00Z"
            }
        }

# Export all models
__all__ = [
    'AgentStatus',
    'ProjectCreate',
    'ProjectResponse',
    'AgentProgressUpdate',
    'ProjectStatus'
] 