from prompt_utils import send_prompt

cot_prompt_business = """Phân tích lợi ích và rủi ro của quyết định kinh doanh sau, hãy suy nghĩ từng bước:
Một công ty đang xem xét mở rộng hoạt động sang thị trường nước ngoài.
Hãy phân tích các lợi ích tiềm năng và rủi ro có thể gặp phải của quyết định này."""

result_business = send_prompt(cot_prompt_business)
print("Chain-of-Thought Business Analysis result:")
print(result_business)
