from anthropic import Anthropic
from ..core.config import get_settings
from ..core.exceptions import AIGenerationError
from typing import Optional, Dict, Any

settings = get_settings()

class AnthropicService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    async def generate_response(
        self, 
        system_prompt: str,
        user_message: str,
        model: str = "claude-3-opus-20240229",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> str:
        """Generate a response using the Anthropic API."""
        try:
            response = await self.client.messages.create(
                model=model,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.content
        except Exception as e:
            raise AIGenerationError(f"Error generating AI response: {str(e)}")

anthropic_service = AnthropicService() 