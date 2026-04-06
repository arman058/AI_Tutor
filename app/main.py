from fastapi import FastAPI
from app.api import tutor_routes, syllabus_routes, session_routes
from app.auth import auth_routes
from app.api import progress_routes
from app.api import dashboard_routes
from app.api import voice_routes

app = FastAPI(
    title="AI Interactive Programming Tutor",
    description="Backend API for AI Tutor System",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "AI Tutor Backend Running"}

# Register routes

app.include_router(auth_routes.router)
app.include_router(tutor_routes.router)
app.include_router(syllabus_routes.router)
app.include_router(progress_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(voice_routes.router)
# app.include_router(session_routes.router)