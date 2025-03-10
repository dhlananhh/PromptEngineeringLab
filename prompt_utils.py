import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

def send_prompt(prompt, system_message=None, model_name='gemini-2.0-flash'):
    """
    Gửi một prompt đến Gemini API và trả về phản hồi.

    Args:
        prompt (str): Nội dung prompt (câu hỏi, yêu cầu).
        system_message (str, optional): Thông điệp hệ thống (hướng dẫn vai trò - hiện tại Gemini-Flash không trực tiếp dùng system message,
                                        nhưng có thể đưa vào prompt). Mặc định: None.
        model_name (str, optional): Model Gemini sử dụng. Mặc định: 'gemini-2.0-flash'.

    Returns:
        str: Phản hồi từ Gemini.
    """
    if system_message:
        # Kết hợp system message và prompt (cách Gemini thường dùng)
        final_prompt = f"{system_message}\n\n{prompt}"
    else:
        final_prompt = prompt

    response = model.generate_content(final_prompt)
    return response.text

if __name__ == "__main__":
    test_prompt = "Giải thích prompt engineering bằng 1 câu."
    result = send_prompt(test_prompt)
    print(result)
