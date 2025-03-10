from prompt_utils import send_prompt

zero_shot_prompt = """
Phân loại đoạn văn sau vào một trong các thể loại: Thể thao, Công nghệ, Giải trí, Chính trị, hoặc Khoa học.
Đoạn văn: 'Apple vừa công bố iPhone mới với chip A16 và camera 48MP cải tiến.'
"""

result = send_prompt(zero_shot_prompt)
print("Zero-shot classification result (Gemini):")
print(result)
