from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from ....models.chat import (
    MessageCreate,
    MessageResponse,
    ConversationCreate,
    ConversationResponse
)
from ....models.responses import HTTPError, HTTPValidationError
from ....services.chat import chat_service
from ...dependencies import get_current_user

router = APIRouter()

@router.post(
    "/conversations",
    response_model=ConversationResponse,
    responses={
        201: {
            "model": ConversationResponse,
            "description": "Conversation created successfully"
        },
        400: {
            "model": HTTPError,
            "description": "Bad request"
        },
        401: {
            "model": HTTPError,
            "description": "Not authenticated"
        },
        422: {
            "model": HTTPValidationError,
            "description": "Validation error"
        }
    },
    status_code=status.HTTP_201_CREATED
)
async def create_conversation(
    conversation: ConversationCreate,
    _=Depends(get_current_user)
) -> ConversationResponse:
    """Create a new conversation."""
    return await chat_service.create_conversation(conversation)

@router.get(
    "/conversations/{conversation_id}",
    response_model=ConversationResponse,
    responses={
        200: {
            "model": ConversationResponse,
            "description": "Conversation retrieved successfully"
        },
        401: {
            "model": HTTPError,
            "description": "Not authenticated"
        },
        404: {
            "model": HTTPError,
            "description": "Conversation not found"
        },
        422: {
            "model": HTTPValidationError,
            "description": "Validation error"
        }
    }
)
async def get_conversation(
    conversation_id: UUID,
    _=Depends(get_current_user)
) -> ConversationResponse:
    """Get a conversation and its messages."""
    return await chat_service.get_conversation(conversation_id)

@router.post(
    "/conversations/{conversation_id}/messages",
    response_model=MessageResponse,
    responses={
        201: {
            "model": MessageResponse,
            "description": "Message created successfully"
        },
        400: {
            "model": HTTPError,
            "description": "Bad request"
        },
        401: {
            "model": HTTPError,
            "description": "Not authenticated"
        },
        404: {
            "model": HTTPError,
            "description": "Conversation not found"
        },
        422: {
            "model": HTTPValidationError,
            "description": "Validation error"
        }
    },
    status_code=status.HTTP_201_CREATED
)
async def create_message(
    conversation_id: UUID,
    message: MessageCreate,
    _=Depends(get_current_user)
) -> MessageResponse:
    """Create a new message in a conversation."""
    return await chat_service.create_message(conversation_id, message)

@router.get(
    "/conversations/{conversation_id}/messages",
    response_model=List[MessageResponse],
    responses={
        200: {
            "model": List[MessageResponse],
            "description": "Messages retrieved successfully"
        },
        401: {
            "model": HTTPError,
            "description": "Not authenticated"
        },
        404: {
            "model": HTTPError,
            "description": "Conversation not found"
        },
        422: {
            "model": HTTPValidationError,
            "description": "Validation error"
        }
    }
)
async def get_messages(
    conversation_id: UUID,
    _=Depends(get_current_user)
) -> List[MessageResponse]:
    """Get all messages in a conversation."""
    return await chat_service.get_messages(conversation_id) 