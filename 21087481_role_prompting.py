from prompt_utils import send_prompt

role_prompt = """Bạn là một chuyên gia dinh dưỡng với hơn 15 năm kinh nghiệm. Hãy đưa ra lời khuyên về chế độ
ăn uống cho một người muốn tăng cường sức khỏe tim mạch."""

system_message = "Bạn là một chuyên gia dinh dưỡng với bằng Tiến sĩ Dinh dưỡng học và 15 năm kinh nghiệm làm việc với bệnh nhân tim mạch."

result = send_prompt(role_prompt, system_message)
print("Role prompting result:")
print(result)
print("\n" + "-"*50 + "\n")
