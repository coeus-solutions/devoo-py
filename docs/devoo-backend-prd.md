# Devoo Backend Technical PRD
Version 1.0 | January 2025

## 1. System Architecture

### 1.1 Technology Stack
- Backend Framework: FastAPI
- Database: Supabase (PostgreSQL)
- AI: Anthropic Claude API
- Project Environment: StackBlitz API
- Authentication: Supabase Auth
- WebSocket: FastAPI WebSocket for real-time updates

### 1.2 High-Level Architecture
```
Client <-> FastAPI Server <-> AI Agent System <-> Anthropic API
  ↕            ↕                    ↕
Supabase    StackBlitz          Message Bus
```

## 2. AI Agent System

### 2.1 Agent Framework
```python
class BaseAgent:
    def __init__(self, client: Anthropic):
        self.client = client
        self.conversation_history = []
        
    async def process(self, message: str) -> str:
        # Base processing logic
        pass

class DevooAgentSystem:
    def __init__(self):
        self.requirements_agent = RequirementsAgent()
        self.architecture_agent = ArchitectureAgent()
        self.implementation_agent = ImplementationAgent()
        self.qa_agent = QAAgent()
```

### 2.2 Agent Specifications

#### 2.2.1 Requirements Agent
**Purpose:** Analyze user requirements and create technical specifications
```python
class RequirementsAgent(BaseAgent):
    async def analyze_requirements(self, user_input: str) -> ProjectSpec:
        system_prompt = """You are a senior software architect.
        Analyze the user requirements and create detailed technical specifications."""
        # Implementation details
```

#### 2.2.2 Architecture Agent
**Purpose:** Design system architecture and component structure with React + TypeScript + Vite

```python
class ArchitectureAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.tech_stack = {
            "framework": "React 18+",
            "language": "TypeScript 5+",
            "bundler": "Vite",
            "styling": "Tailwind CSS",
            "state": "Zustand/Jotai",
            "form": "React Hook Form + Zod",
            "components": "shadcn/ui"
        }
        
    async def design_architecture(self, project_spec: ProjectSpec) -> Architecture:
        system_prompt = """You are an expert frontend architect specializing in React + TypeScript applications.
        
        Technical Requirements:
        - Use Vite for build tooling
        - Implement strict TypeScript configuration
        - Follow React 18+ best practices
        - Ensure component reusability and modularity
        - Implement proper state management patterns
        
        Design Guidelines:
        1. Visual Hierarchy:
           - Clear content structure
           - Consistent spacing system
           - Thoughtful typography scale
           - Purposeful color usage
        
        2. Component Architecture:
           - Atomic Design principles
           - Composition over inheritance
           - Proper prop typing
           - Custom hook extraction
        
        3. Styling Approach:
           - Tailwind CSS for utility-first styling
           - CSS variables for theming
           - Mobile-first responsive design
           - Dark mode support
        
        4. Performance Considerations:
           - Code splitting
           - Lazy loading
           - Memoization when needed
           - Asset optimization
        
        5. User Experience:
           - Loading states
           - Error boundaries
           - Form validation
           - Accessibility compliance
        
        6. State Management:
           - Zustand for global state
           - Jotai for atomic state
           - React Query for server state
           - Context for theme/auth
        
        Project Structure:
        ```
        src/
        ├── assets/          # Static files
        ├── components/      # Reusable components
        │   ├── ui/         # Base components
        │   ├── forms/      # Form components
        │   └── layouts/    # Layout components
        ├── features/        # Feature-based modules
        ├── hooks/          # Custom hooks
        ├── lib/            # Utility functions
        ├── pages/          # Route components
        ├── services/       # API services
        ├── stores/         # State management
        ├── styles/         # Global styles
        └── types/          # TypeScript types
        ```
        
        Generate an architecture that follows these guidelines while adapting to the specific project requirements."""
        
    async def setup_vite_config(self) -> str:
        return """
        import { defineConfig } from 'vite';
        import react from '@vitejs/plugin-react-swc';
        import path from 'path';

        export default defineConfig({
          plugins: [react()],
          resolve: {
            alias: {
              '@': path.resolve(__dirname, './src')
            }
          },
          build: {
            sourcemap: true,
            chunkSizeWarningLimit: 1000
          }
        });
        """
    
    async def setup_typescript_config(self) -> str:
        return """
        {
          "compilerOptions": {
            "target": "ES2020",
            "useDefineForClassFields": true,
            "lib": ["ES2020", "DOM", "DOM.Iterable"],
            "module": "ESNext",
            "skipLibCheck": true,
            "moduleResolution": "bundler",
            "allowImportingTsExtensions": true,
            "resolveJsonModule": true,
            "isolatedModules": true,
            "noEmit": true,
            "jsx": "react-jsx",
            "strict": true,
            "noUnusedLocals": true,
            "noUnusedParameters": true,
            "noFallthroughCasesInSwitch": true,
            "baseUrl": ".",
            "paths": {
              "@/*": ["./src/*"]
            }
          },
          "include": ["src"],
          "references": [{ "path": "./tsconfig.node.json" }]
        }
        """
```

The Architecture Agent will:
1. Design the application structure based on project requirements
2. Generate necessary configuration files (vite.config.ts, tsconfig.json)
3. Set up the project with proper TypeScript configuration
4. Implement design system and component architecture
5. Configure build and development tooling
6. Establish coding standards and best practices

#### 2.2.3 Implementation Agent
**Purpose:** Generate code and implement features
```python
class ImplementationAgent(BaseAgent):
    async def generate_code(self, architecture: Architecture) -> CodeBase:
        system_prompt = """You are an expert React developer.
        Generate clean, maintainable code following best practices."""
        # Implementation details
```

#### 2.2.4 QA Agent
**Purpose:** Review code and fix issues
```python
class QAAgent(BaseAgent):
    async def review_code(self, code: CodeBase) -> ReviewResult:
        system_prompt = """You are a senior QA engineer.
        Review code for best practices and potential issues."""
        # Implementation details
```

### 2.3 Agent Coordination
```python
class AgentCoordinator:
    async def orchestrate_project_creation(self, user_input: str):
        # 1. Requirements Analysis
        project_spec = await requirements_agent.analyze_requirements(user_input)
        
        # 2. Architecture Design
        architecture = await architecture_agent.design_architecture(project_spec)
        
        # 3. Implementation
        codebase = await implementation_agent.generate_code(architecture)
        
        # 4. QA Review
        review = await qa_agent.review_code(codebase)
```

## 3. Database Schema (Supabase)

### 3.1 Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE,
    preferences JSONB DEFAULT '{}'::jsonb
);
```

### 3.2 Projects Table
```sql
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    name TEXT NOT NULL,
    description TEXT,
    requirements TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    status TEXT DEFAULT 'draft',
    stackblitz_id TEXT,
    settings JSONB DEFAULT '{}'::jsonb
);
```

### 3.3 Conversations Table
```sql
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 3.4 Messages Table
```sql
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conversation_id UUID REFERENCES conversations(id),
    role TEXT NOT NULL, -- 'user' or 'assistant'
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    metadata JSONB DEFAULT '{}'::jsonb
);
```

### 3.5 CodeVersions Table
```sql
CREATE TABLE code_versions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(id),
    version INT NOT NULL,
    files JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    commit_message TEXT,
    metadata JSONB DEFAULT '{}'::jsonb
);
```

## 4. API Endpoints and Real-time Updates

### 4.1 Data Models
```python
class AgentStatus(str, Enum):
    QUEUED = "queued"
    ANALYZING = "analyzing"
    DESIGNING = "designing"
    IMPLEMENTING = "implementing"
    REVIEWING = "reviewing"
    COMPLETED = "completed"
    ERROR = "error"

class AgentProgressUpdate(BaseModel):
    agent_type: str
    status: AgentStatus
    message: str
    progress: float  # 0 to 1
    metadata: Dict[str, Any] = {}

class ProjectStatus(BaseModel):
    current_agent: str
    overall_progress: float
    stage_progress: float
    status_message: str
    last_update: datetime
```

### 4.2 Project Management
```python
@router.post("/projects/")
async def create_project(project: ProjectCreate) -> ProjectResponse:
    """Create a new project and initialize agents"""
    project_id = await db.create_project(project)
    await progress_manager.initialize_project(project_id)
    return {"project_id": project_id, "status": "initialized"}

@router.get("/projects/{project_id}")
async def get_project(project_id: UUID) -> ProjectDetails:
    """Get project details including current status"""
    project = await db.get_project(project_id)
    status = await progress_manager.get_project_status(project_id)
    return {**project, "status": status}

@router.get("/projects/{project_id}/status")
async def get_project_status(project_id: UUID) -> ProjectStatus:
    """Get current project status and progress"""
    return await progress_manager.get_project_status(project_id)
```

### 4.3 Real-time Progress Updates
```python
class ProgressManager:
    def __init__(self):
        self.active_connections: Dict[UUID, List[WebSocket]] = defaultdict(list)
        self.project_status: Dict[UUID, ProjectStatus] = {}

    async def broadcast_update(self, project_id: UUID, update: AgentProgressUpdate):
        """Broadcast progress update to all connected clients"""
        for connection in self.active_connections[project_id]:
            await connection.send_json(update.dict())

@router.websocket("/projects/{project_id}/progress")
async def project_progress_websocket(
    websocket: WebSocket,
    project_id: UUID,
    current_user: User = Depends(get_current_user)
):
    """WebSocket connection for real-time progress updates"""
    await websocket.accept()
    progress_manager.active_connections[project_id].append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except WebSocketDisconnect:
        progress_manager.active_connections[project_id].remove(websocket)
```

### 4.4 Agent Interaction
```python
@router.post("/projects/{project_id}/generate")
async def generate_code(
    project_id: UUID,
    background_tasks: BackgroundTasks
) -> ProjectStatus:
    """Start the code generation process"""
    background_tasks.add_task(agent_coordinator.start_generation, project_id)
    return await progress_manager.get_project_status(project_id)

class AgentCoordinator:
    async def start_generation(self, project_id: UUID):
        """Coordinate agents and send progress updates"""
        try:
            # Requirements Analysis
            await self._update_progress(project_id, {
                "agent_type": "requirements",
                "status": AgentStatus.ANALYZING,
                "message": "Analyzing project requirements...",
                "progress": 0.1
            })
            project_spec = await requirements_agent.analyze_requirements(user_input)

            # Architecture Design
            await self._update_progress(project_id, {
                "agent_type": "architecture",
                "status": AgentStatus.DESIGNING,
                "message": "Designing system architecture...",
                "progress": 0.3
            })
            architecture = await architecture_agent.design_architecture(project_spec)

            # Code Implementation
            await self._update_progress(project_id, {
                "agent_type": "implementation",
                "status": AgentStatus.IMPLEMENTING,
                "message": "Generating code...",
                "progress": 0.6
            })
            codebase = await implementation_agent.generate_code(architecture)

            # QA Review
            await self._update_progress(project_id, {
                "agent_type": "qa",
                "status": AgentStatus.REVIEWING,
                "message": "Reviewing generated code...",
                "progress": 0.9
            })
            review = await qa_agent.review_code(codebase)

            # Complete
            await self._update_progress(project_id, {
                "agent_type": "system",
                "status": AgentStatus.COMPLETED,
                "message": "Project generated successfully!",
                "progress": 1.0
            })

        except Exception as e:
            await self._update_progress(project_id, {
                "agent_type": "system",
                "status": AgentStatus.ERROR,
                "message": f"Error: {str(e)}",
                "progress": 0
            })

    async def _update_progress(
        self,
        project_id: UUID,
        update: Dict[str, Any]
    ):
        progress_update = AgentProgressUpdate(**update)
        await progress_manager.broadcast_update(project_id, progress_update)
```

### 4.5 StackBlitz Integration
```python
@router.post("/projects/{project_id}/preview")
async def create_preview(
    project_id: UUID,
    background_tasks: BackgroundTasks
) -> Dict[str, str]:
    """Create and update StackBlitz preview"""
    # Start preview creation
    await progress_manager.broadcast_update(
        project_id,
        AgentProgressUpdate(
            agent_type="preview",
            status=AgentStatus.IMPLEMENTING,
            message="Setting up StackBlitz preview...",
            progress=0.8
        )
    )

    stackblitz_url = await stackblitz_service.create_project(
        name=f"devoo-{project_id}",
        files=await code_manager.get_project_files(project_id)
    )

    # Update preview status
    await progress_manager.broadcast_update(
        project_id,
        AgentProgressUpdate(
            agent_type="preview",
            status=AgentStatus.COMPLETED,
            message="Preview ready!",
            progress=1.0,
            metadata={"preview_url": stackblitz_url}
        )
    )

    return {"preview_url": stackblitz_url}
```

## 5. Integration Specifications

### 5.1 Anthropic API Integration
```python
class AnthropicService:
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
    
    async def generate_response(self, 
                              system_prompt: str,
                              user_message: str,
                              model: str = "claude-3-opus-20240229") -> str:
        response = await self.client.messages.create(
            model=model,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )
        return response.content
```

### 5.2 StackBlitz Integration
```python
class StackBlitzService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.stackblitz.com/v1"
    
    async def create_project(self, name: str, files: Dict[str, str]) -> str:
        # Create new project
        pass
    
    async def update_project(self, project_id: str, files: Dict[str, str]):
        # Update project files
        pass
```

## 6. Error Handling

### 6.1 Error Types
```python
class DevooError(Exception):
    pass

class AIGenerationError(DevooError):
    pass

class StackBlitzError(DevooError):
    pass

class DatabaseError(DevooError):
    pass
```

### 6.2 Error Handling Middleware
```python
@app.exception_handler(DevooError)
async def devoo_error_handler(request: Request, exc: DevooError):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )
```

## 7. Security Considerations

### 7.1 Authentication
- Supabase JWT tokens
- Role-based access control
- API key management

### 7.2 Data Protection
- Input sanitization
- Rate limiting
- Data encryption

## 8. Monitoring and Logging

### 8.1 Metrics
- API response times
- AI generation times
- Error rates
- User activity

### 8.2 Logging
- Request/Response logging
- Error tracking
- AI agent interactions
- System events