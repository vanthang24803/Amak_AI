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


@router.post("/analytic/statistic" , tags=["analytic"])
async def analytic(request: AskPrompt):
    prompt = f"""
    Bạn là một AI Phân tích dữ liệu 
    - Chỉ trả lời bằng tiếng Việt.
    - Dựa vào các dữ liệu đã gửi hãy phân tích chi tiết dữ liệu tăng giảm
    - Nếu isStock là false thì đó là % giảm so với tháng trước tương ứng với stock ví dụ isStock là false và stock là 20% là giảm 20% so với tháng trước , total là tổng số dữ liệu trong tháng hiện tại hãy đưa ra các nhận xét về việc kinh doanh trong tháng hiện tại 
    - Có thể viết thành 1 bài phân tích ngắn không được nói chuyện dở dang khoảng 1000 ký tự
    Vui lòng phân tích dữ liệu sau: {request.prompt}
    """

    try:
        response = model.generate_content(prompt)  
        return Response.send(200, message=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analytic/chart" , tags=["analytic"])
async def analytic_chart(request:AskPrompt):
    prompt = f"""
    Bạn là một AI Phân tích dữ liệu 
    - Chỉ trả lời bằng tiếng Việt.
    - Dựa vào các dữ liệu đã gửi hãy phân tích chi tiết dữ liệu tăng giảm
    - Đây là dữ liệu tổng doanh thu trong các thời điểm trong năm với year month week đều là tháng hiện tại hãy đưa ra các phân tích theo từng
    mục thời gian rồi tóm lại tổng quát 
    - Có thể viết thành 1 bài phân tích ngắn không được nói chuyện dở dang khoảng 1000 ký tự
    Vui lòng phân tích dữ liệu sau: {request.prompt}
    """

    try:
        response = model.generate_content(prompt)  
        return Response.send(200, message=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analytic/review", tags=["analytic"])
async def analytic_review(request:AskPrompt):
    prompt = f"""
    Bạn là một AI Phân tích dữ liệu 
    - Chỉ trả lời bằng tiếng Việt.
    - Dựa vào các dữ liệu đã gửi hãy phân tích và đưa ra đánh giá về các review đơn hàng hãy đưa ra phân tích chung về các review tốt và xấu của sản phẩm và đưa ra số liệu trung bình đây là 1 sản phẩm tốt hay xấu đáng mua hay kh    ông ?
    - Có thể viết thành 1 bài phân tích ngắn không được nói chuyện dở dang khoảng 500 ký tự
    Vui lòng phân tích dữ liệu sau: {request.prompt}
    """

    try:
        response = model.generate_content(prompt)  
        return Response.send(200, message=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)