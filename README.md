# Devoo Backend

A FastAPI-based backend service for Devoo, providing AI-powered development assistance and project management capabilities.

## Features

- Authentication and authorization using Supabase
- AI-powered development assistance using Anthropic's Claude
- Project management and chat functionality
- Real-time communication capabilities
- Structured API responses and error handling

## Prerequisites

- Python 3.9+
- PostgreSQL (via Supabase)
- Supabase account
- Anthropic API access
- Perplexity API access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/coeus-solutions/devoo-py.git
cd devoo-py
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` with your actual credentials:
- Supabase credentials
- Anthropic API key
- Perplexity API key

## Project Structure

```
src/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── routers/
│   │   │   │   ├── auth.py
│   │   │   │   ├── chat.py
│   │   │   │   └── projects.py
│   │   │   └── router.py
│   │   └── dependencies.py
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── prompts/
│   ├── models/
│   │   ├── auth.py
│   │   ├── chat.py
│   │   └── schemas.py
│   └── services/
│       ├── agent_system.py
│       ├── anthropic_service.py
│       ├── auth.py
│       └── supabase.py
└── main.py
```

## Running the Application

1. Start the development server:
```bash
uvicorn src.main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Documentation

The API is organized into the following main endpoints:

- `/api/v1/auth/*` - Authentication and user management
- `/api/v1/projects/*` - Project management endpoints
- `/api/v1/chat/*` - AI chat and assistance endpoints

For detailed API documentation, please refer to the Swagger UI or ReDoc interfaces when running the application.

## Development

1. Follow the code structure and organization
2. Use type hints everywhere
3. Write tests for new functionality
4. Follow FastAPI best practices
5. Handle errors appropriately
6. Document new endpoints

## Environment Variables

Required environment variables (see `.env.example`):

```
# Supabase settings
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
SUPABASE_JWT_TOKEN=your_supabase_jwt_token

# AI API settings
ANTHROPIC_API_KEY=your_anthropic_api_key
PERPLEXITY_API_KEY=your_perplexity_api_key
```

## License

[Add your license information here]

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For support, please contact ashaheen@workhub.ai