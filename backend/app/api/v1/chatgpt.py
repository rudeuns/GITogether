from fastapi import APIRouter, HTTPException
from app.schemas.chatgpt import ChatRequest, ChatResponse
from app.services.chatgpt import create_chat_completions

router = APIRouter()


@router.post("/chatgpt", response_model=ChatResponse, tags=["Chat"])
async def get_chatgpt_response(request: ChatRequest):
    try:
        response = create_chat_completions(request.prompt)
        return ChatResponse(response=response)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
