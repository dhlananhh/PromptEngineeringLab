import os
import google.generativeai as genai
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

# Khởi tạo Gemini API client với API key từ biến môi trường
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Chọn model Gemini (ví dụ: gemini-pro)
model = genai.GenerativeModel('gemini-2.0-flash')

def test_connection_gemini():
    """
    Kiểm tra kết nối API Gemini bằng cách gửi một prompt đơn giản.
    """
    try:
        response = model.generate_content("Xin chào, tôi đang kiểm tra kết nối API Gemini!")
        print("Kết nối Gemini thành công!")
        print("Phản hồi từ Gemini:", response.text)
    except Exception as e:
        print("Có lỗi xảy ra:", e)

# Gọi hàm test_connection_gemini để kiểm tra
test_connection_gemini()
