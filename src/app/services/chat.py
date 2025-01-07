from typing import List, Dict, Any
from uuid import UUID
from ..models.chat import MessageCreate, ConversationCreate, MessageResponse, ConversationResponse
from .supabase import service_role_client
from fastapi import HTTPException
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self):
        self.client = service_role_client

    async def create_conversation(self, conversation_data: ConversationCreate) -> ConversationResponse:
        """Create a new conversation."""
        try:
            result = self.client.table("conversations").insert({
                "project_id": str(conversation_data.project_id)
            }).execute()

            if not result.data:
                raise HTTPException(status_code=400, detail="Failed to create conversation")

            return ConversationResponse(**result.data[0], messages=[])

        except Exception as e:
            logger.error(f"Create conversation error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))

    async def get_conversation(self, conversation_id: UUID) -> ConversationResponse:
        """Get a conversation and its messages."""
        try:
            # Get conversation
            conv_result = self.client.table("conversations").select("*").eq("id", str(conversation_id)).single().execute()
            
            if not conv_result.data:
                raise HTTPException(status_code=404, detail="Conversation not found")

            # Get messages for this conversation
            msg_result = self.client.table("messages").select("*").eq("conversation_id", str(conversation_id)).execute()
            
            # Convert to response model
            messages = [MessageResponse(**msg) for msg in msg_result.data]
            return ConversationResponse(**conv_result.data, messages=messages)

        except Exception as e:
            logger.error(f"Get conversation error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))

    async def create_message(self, conversation_id: UUID, message_data: MessageCreate) -> MessageResponse:
        """Create a new message in a conversation."""
        try:
            # First verify conversation exists
            conv_exists = self.client.table("conversations").select("id").eq("id", str(conversation_id)).single().execute()
            
            if not conv_exists.data:
                raise HTTPException(status_code=404, detail="Conversation not found")

            # Create message
            result = self.client.table("messages").insert({
                "conversation_id": str(conversation_id),
                "content": message_data.content,
                "role": message_data.role,
                "metadata": message_data.metadata
            }).execute()

            if not result.data:
                raise HTTPException(status_code=400, detail="Failed to create message")

            return MessageResponse(**result.data[0])

        except Exception as e:
            logger.error(f"Create message error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))

    async def get_messages(self, conversation_id: UUID) -> List[MessageResponse]:
        """Get all messages in a conversation."""
        try:
            result = self.client.table("messages").select("*").eq("conversation_id", str(conversation_id)).execute()
            return [MessageResponse(**msg) for msg in result.data]

        except Exception as e:
            logger.error(f"Get messages error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))

chat_service = ChatService() 