from fastapi import APIRouter, FastAPI, HTTPException
import os
from dotenv import load_dotenv
import google.generativeai as genai
from ..helpers import AskPrompt, Response

app = FastAPI()
router = APIRouter()
load_dotenv()

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


@router.post("/ask" , tags=["ask"])
async def ask_ai(request: AskPrompt):
    prompt = f"""
    Bạn là một AI hỗ trợ trả lời câu hỏi. 
    - Chỉ trả lời bằng tiếng Việt.
    - Độ dài câu trả lời tối đa là 200 ký tự.
    Vui lòng trả lời câu hỏi sau: {request.prompt}
    """

    try:
        response = model.generate_content(prompt)  
        return Response.send(200, message=response.text[:200])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



app.include_router(router)