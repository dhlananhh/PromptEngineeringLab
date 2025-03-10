from prompt_utils import send_prompt

cot_prompt_probability = """Giải bài toán xác suất sau, hãy suy nghĩ từng bước:
Trong một hộp có 5 viên bi đỏ và 3 viên bi xanh. Nếu bạn lấy ngẫu nhiên 2 viên bi từ hộp,
xác suất để cả 2 viên bi đều màu đỏ là bao nhiêu?"""

result_probability = send_prompt(cot_prompt_probability)
print("Chain-of-Thought Probability result:")
print(result_probability)
