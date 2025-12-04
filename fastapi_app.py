from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine
from backend.routers import experts

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ImplementAI Backend", version="1.0.0")

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "https://tbhrc.github.io",
    "https://implementai.ae",
    "https://www.implementai.ae",
    "https://xva.ae",
    "https://www.xva.ae",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(experts.router, prefix="/api")


@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
