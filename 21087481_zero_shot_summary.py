from prompt_utils import send_prompt

zero_shot_prompt_summary = """
Tóm tắt đoạn văn sau trong 2-3 câu.
Đoạn văn: 'Ngày nay, biến đổi khí hậu là một trong những thách thức lớn nhất mà nhân loại phải đối mặt.
Nhiệt độ toàn cầu đang tăng lên, mực nước biển dâng cao, và các hiện tượng thời tiết cực đoan
trở nên thường xuyên và khốc liệt hơn.  Để giảm thiểu tác động của biến đổi khí hậu, chúng ta cần
hành động mạnh mẽ để giảm phát thải khí nhà kính và chuyển đổi sang các nguồn năng lượng tái tạo.'
"""

result_summary = send_prompt(zero_shot_prompt_summary)
print("Zero-shot Summary result:")
print(result_summary)
