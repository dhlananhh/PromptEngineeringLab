from prompt_utils import send_prompt

few_shot_prompt_headline = """
Tạo tiêu đề bài báo hấp dẫn, ngắn gọn từ nội dung cho trước.

Ví dụ 1:
Nội dung: 'Giá xăng tiếp tục tăng mạnh trong tuần này, gây lo ngại cho người tiêu dùng.'
Tiêu đề: 'Giá xăng leo thang: "Bão giá" giáng đòn vào túi tiền người dân'

Ví dụ 2:
Nội dung: 'Một nhóm nhà khoa học vừa phát hiện ra một hành tinh mới có khả năng tồn tại sự sống ngoài Trái Đất.'
Tiêu đề: 'Kinh ngạc: Phát hiện hành tinh "anh em" của Trái Đất, có thể có sự sống!'

Nội dung cần tạo tiêu đề: 'Tổng sản phẩm quốc nội (GDP) của Việt Nam tăng trưởng 6.5% trong năm nay, vượt mục tiêu đề ra.'
Tiêu đề:
"""

result_headline = send_prompt(few_shot_prompt_headline)
print("Few-shot Headline Generation result:")
print(result_headline)
