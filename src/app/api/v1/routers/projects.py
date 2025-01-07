from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from typing import Dict, Any
from uuid import UUID
from ....models.schemas import (
    ProjectCreate, 
    ProjectResponse, 
    ProjectStatus,
    AgentProgressUpdate
)
from ....models.responses import HTTPError, HTTPValidationError
from ....services.agent_system import agent_coordinator
from ....services.supabase import create_client
from ....core.config import get_settings

router = APIRouter()
settings = get_settings()

@router.post(
    "/",
    response_model=ProjectResponse,
    responses={
        201: {"description": "Project created successfully"},
        400: {"model": HTTPError, "description": "Bad request"},
        401: {"model": HTTPError, "description": "Not authenticated"},
        422: {"model": HTTPValidationError, "description": "Validation error"}
    },
    status_code=status.HTTP_201_CREATED
)
async def create_project(
    project: ProjectCreate,
    background_tasks: BackgroundTasks
) -> ProjectResponse:
    """Create a new project and initialize agents"""
    try:
        # Create a fresh service role client
        service_client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_SERVICE_ROLE_KEY
        )
        
        # Create project in Supabase using service role client
        data = {
            "name": project.name,
            "description": project.description,
            "requirements": project.requirements,
            "status": "initialized",
            "settings": project.settings,
            "user_id": "49734f1d-97d0-4e54-a84a-9e9101cb7693"  # Hardcoded user ID for development
        }
        
        result = service_client.table("projects").insert(data).execute()
        project_data = result.data[0]
        
        # Start the generation process in background
        background_tasks.add_task(
            agent_coordinator.start_generation,
            project_data["id"]
        )
        
        return ProjectResponse(**project_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    responses={
        200: {"description": "Project retrieved successfully"},
        401: {"model": HTTPError, "description": "Not authenticated"},
        404: {"model": HTTPError, "description": "Project not found"},
        422: {"model": HTTPValidationError, "description": "Validation error"}
    }
)
async def get_project(project_id: UUID) -> ProjectResponse:
    """Get project details"""
    try:
        # Create a fresh service role client
        service_client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_SERVICE_ROLE_KEY
        )
        
        result = service_client.table("projects").select("*").eq("id", str(project_id)).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Project not found")
        return ProjectResponse(**result.data[0])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/{project_id}/status",
    response_model=ProjectStatus,
    responses={
        200: {"description": "Project status retrieved successfully"},
        401: {"model": HTTPError, "description": "Not authenticated"},
        404: {"model": HTTPError, "description": "Project not found"},
        422: {"model": HTTPValidationError, "description": "Validation error"}
    }
)
async def get_project_status(project_id: UUID) -> ProjectStatus:
    """Get current project status and progress"""
    try:
        # Create a fresh service role client
        service_client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_SERVICE_ROLE_KEY
        )
        
        result = service_client.table("projects").select("*").eq("id", str(project_id)).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Project not found")
        
        project = result.data[0]
        
        # Create a ProjectStatus response with default values
        return ProjectStatus(
            current_agent="initializing",
            overall_progress=0.0,
            stage_progress=0.0,
            status_message=f"Project is in {project['status']} state",
            last_update=project['updated_at']
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 