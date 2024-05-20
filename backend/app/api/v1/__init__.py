from fastapi import APIRouter
from .chatgpt import router as chat_router

router = APIRouter()

router.include_router(chat_router, prefix="/api/v1")
