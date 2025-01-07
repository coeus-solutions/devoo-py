from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional, Dict, Any

class MessageCreate(BaseModel):
    content: str
    role: str = "user"  # default to user, can be 'user' or 'assistant'
    metadata: Dict[str, Any] = {}

class MessageResponse(BaseModel):
    id: UUID4
    conversation_id: UUID4
    content: str
    role: str
    created_at: datetime
    metadata: Dict[str, Any]

class ConversationCreate(BaseModel):
    project_id: UUID4

class ConversationResponse(BaseModel):
    id: UUID4
    project_id: UUID4
    created_at: datetime
    updated_at: datetime
    messages: List[MessageResponse] = [] 