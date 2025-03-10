from prompt_utils import send_prompt

role_prompt_psychologist = """Bạn là một chuyên gia tâm lý, am hiểu về các vấn đề căng thẳng và stress trong cuộc sống hiện đại.
Hãy đưa ra 3 lời khuyên hữu ích nhất để một người có thể đối phó với stress hiệu quả hơn."""

system_message_psychologist = "Bạn là Tiến sĩ Tâm lý học, có kinh nghiệm 20 năm tư vấn và trị liệu tâm lý."

result_psychologist = send_prompt(role_prompt_psychologist, system_message=system_message_psychologist)
print("Role Prompting - Psychologist result:")
print(result_psychologist)
