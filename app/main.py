from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import get_db
from app.example_module.apis import router as example_router
from app.users.apis import router as user_router

app = FastAPI(
    title="Heavyweight(FastAPI)",
    docs_url="/",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1
    },  # Hides Schemas Menu in DocsF
)

# Variables for CORS
origins = ["*"]

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health Check Route
@app.get("/health", status_code=200, include_in_schema=False)
def health_check(db=Depends(get_db)):
    return {"status": "ok"}


# Routers for the API
app.include_router(example_router, prefix="/example", tags=["Example Docs"])
app.include_router(user_router, prefix="/users", tags=["User Docs"])
