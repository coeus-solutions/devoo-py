from .requirements_agent import REQUIREMENTS_PROMPTS
from .architecture_agent import ARCHITECTURE_PROMPTS
from .implementation_agent import IMPLEMENTATION_PROMPTS
from .qa_agent import QA_PROMPTS

class PromptsManager:
    def __init__(self):
        self.prompts = {
            "requirements": REQUIREMENTS_PROMPTS,
            "architecture": ARCHITECTURE_PROMPTS,
            "implementation": IMPLEMENTATION_PROMPTS,
            "qa": QA_PROMPTS
        }
    
    def get_prompt(self, agent_type: str, prompt_key: str) -> str:
        """Get a specific prompt for an agent type."""
        if agent_type not in self.prompts:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        prompts = self.prompts[agent_type]
        if prompt_key not in prompts:
            raise ValueError(f"Unknown prompt key: {prompt_key} for agent {agent_type}")
        
        return prompts[prompt_key]

prompts_manager = PromptsManager() 