from prompt_utils import send_prompt

prompt_for_definition = "What is role prompting?"

response_definition = send_prompt(prompt_for_definition)

print("Question: ", prompt_for_definition)
print("\nGemini's response to 'What is role prompting?':")
print(response_definition)
