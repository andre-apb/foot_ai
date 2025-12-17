# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development Environment
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application (development)
python3 app/run.py

# Run the application (production with gunicorn)
gunicorn -w 32 -b 0.0.0.0:5000 app:app
```

### Testing
```bash
# Run all tests
python3 -m pytest

# Run tests with verbose output
python3 -m pytest -v

# Run tests with coverage
python3 -m pytest --cov=app --cov-report=term-missing

# Run specific test file
python3 -m pytest tests/services/test_create_user_service.py

# Run specific test
python3 -m pytest tests/services/test_create_user_service.py::TestCreateUserService::test_execute_creates_user
```

## Architecture Overview

### Service Layer Pattern
The application follows a strict service layer pattern where all business logic is encapsulated in service classes:

- Each service has a single responsibility
- Services accept a database session in their constructor
- All services implement an `execute()` method
- Services are located in `app/services/` organized by domain

Example service pattern:
```python
class CreateUserService:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, **kwargs) -> User:
        # Business logic here
        user = User(**kwargs)
        self.session.add(user)
        self.session.flush()  # Get ID without committing
        return user
```

### API Layer
- Single Blueprint (`api_bp`) in `app/views/api.py`
- Session management using context managers
- Services are instantiated within request context

### Testing Patterns
- Use Factory Boy for all model factories (see `tests/factories.py`)
- Mock all external dependencies (Supabase, Stripe, FAL, etc.)
- When testing API endpoints, mock the service layer, not the implementation
- Test files mirror the application structure

### Key Project Rules
- Clean Architecture: Strict separation of concerns
- No long functions: Break logic into smaller units
- Avoid excessive try-catch: Let exceptions bubble up
- No redundant comments: Write self-explanatory code
- Mock external dependencies in tests
- Use Factory Boy for test data generation

### External Services Integration
- **Sentry**: Error tracking (production only)

### Environment Configuration
The application uses environment variables for configuration. Key variables include:
- `SENTRY_DSN`: Sentry error tracking (production)
