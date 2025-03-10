from prompt_utils import send_prompt

cot_prompt = """Giải bài toán sau đây, hãy suy nghĩ từng bước:
Một cửa hàng bán 5 loại trái cây: táo, cam, nho, chuối và dưa hấu. Giá của mỗi loại lần lượt là 15.000đ, 20.
000đ, 35.000đ, 12.000đ và 40.000đ mỗi kg. Nếu mua 2kg táo, 1.5kg cam, 0.5kg nho, 3kg chuối và 4kg dưa hấu, tổng
số tiền cần trả là bao nhiêu?"""

result = send_prompt(cot_prompt)
print("Chain-of-Thought result:")
print(result)
print("\n" + "-"*50 + "\n")
