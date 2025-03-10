from prompt_utils import send_prompt

role_prompt_writer = """Bạn là một nhà văn nổi tiếng, phong cách viết lãng mạn và giàu cảm xúc.
Hãy viết một đoạn mở đầu cho một truyện ngắn tình yêu buồn, khoảng 3-4 câu."""

system_message_writer = "Bạn là Nguyễn Nhật Ánh, nhà văn Việt Nam nổi tiếng với những truyện ngắn, truyện dài lãng mạn."

result_writer = send_prompt(role_prompt_writer, system_message=system_message_writer)
print("Role Prompting - Writer result:")
print(result_writer)
