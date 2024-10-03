from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import AskAIRoute, AnalyticRoute

app = FastAPI(
    title="Amak",
    version="1.0.0",
    docs_url="/docs"
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AskAIRoute)
app.include_router(AnalyticRoute)
