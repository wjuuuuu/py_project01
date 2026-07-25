import os
from openai import OpenAI

# 创建与 AI 大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量名字，值就是 DeepSeek 的 API——KEY 的)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 与 AI 大模型进行交互（）
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个非常可爱的 AI 助理，你的名字叫小甜甜，请你使用温柔的语气回答用户问题."},
        {"role": "user", "content": "你是谁，你能帮我做什么？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出大模型返回的结果
print(response.choices[0].message.content)