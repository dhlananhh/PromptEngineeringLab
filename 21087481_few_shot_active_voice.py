from prompt_utils import send_prompt

few_shot_prompt_active = """
Chuyển các câu sau từ thể bị động sang thể chủ động.

Ví dụ 1:
Câu bị động: 'Bài tập về nhà đã được làm bởi học sinh.'
Câu chủ động: 'Học sinh đã làm bài tập về nhà.'

Ví dụ 2:
Câu bị động: 'Chiếc bánh đã bị ăn bởi con mèo.'
Câu chủ động: 'Con mèo đã ăn chiếc bánh.'

Câu bị động cần chuyển: 'Ngôi nhà mới sẽ được xây dựng bởi công ty xây dựng.'
Câu chủ động:
"""

result_active = send_prompt(few_shot_prompt_active)
print("Few-shot Active Voice Conversion result:")
print(result_active)
