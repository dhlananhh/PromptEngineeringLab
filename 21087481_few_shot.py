from prompt_utils import send_prompt

few_shot_prompt = """
Phân loại đoạn văn sau vào một trong các thể loại: Thể thao, Công nghệ, Giải trí, Chính trị, hoặc Khoa học.

Ví dụ 1:
Đoạn văn: 'Đội tuyển Việt Nam đã giành chiến thắng 2-1 trước Malaysia trong trận đấu tối qua.'
Phân loại: Thể thao

Ví dụ 2:
Đoạn văn: 'NASA phóng tàu vũ trụ mới để khám phá sao Hỏa, dự kiến sẽ đáp xuống bề mặt trong 6 tháng tới.'
Phân loại: Khoa học

Đoạn văn cần phân loại: 'Chính phủ vừa thông qua dự luật mới về cải cách thuế trong phiên họp quốc hội.'
Phân loại:
"""

result = send_prompt(few_shot_prompt)
print("Few-shot classification result (Gemini):")
print(result)
print("\n" + "-"*50 + "\n")
