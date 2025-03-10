from prompt_utils import send_prompt

zero_shot_prompt_sentiment = """
Phân tích tình cảm của bình luận sau đây. Cho biết bình luận mang tính Tích cực, Tiêu cực hay Trung lập.
Bình luận: 'Sản phẩm này thật tệ, tôi rất thất vọng. Đừng ai mua!'
"""

result_sentiment = send_prompt(zero_shot_prompt_sentiment)
print("Zero-shot Sentiment Analysis result:")
print(result_sentiment)
