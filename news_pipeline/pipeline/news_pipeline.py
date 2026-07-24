from news_pipeline.processors.ai_news_processor import AINewsProcessor
from news_pipeline.providers.openai_image_provider import OpenAIImageProvider
from news_pipeline.publishers.telegram_bot_publisher import TelegramBotPublisher
import os
JSON_PROMPT = ('You are a professional Arabic news editor. '
 'Instructions: 1) Rewrite professionally in Arabic; never copy original wording. '
 '2) Preserve facts exactly; never hallucinate. '
 '3) Attribute unverified claims: use "بحسب..." / "وفقًا لـ...". '
 '4) Generate a short engaging Arabic headline. '
 '5) Write a 2-4 paragraph professional news article. '
 '6) Remove Telegram formatting, hashtags, unnecessary emojis. '
 '7) Generate a detailed English image prompt. '
 '8) Return ONLY strict JSON: {"headline_1":"...","arabic_article":"...","image_prompt_en":"..."}. '
 'No markdown, no prose, no explanations.')
class NewsPipeline:
    def __init__(self):
        from ai.openai_provider import OpenAIProvider
        self.ai = AINewsProcessor(OpenAIProvider())
        self.img = OpenAIImageProvider()
        self.pub = TelegramBotPublisher()
    async def run(self, text):
        data = await self.ai.process(text, prompt=JSON_PROMPT)
        url = None
        payload = {"caption": f"{data['headline_1']}\n{data['arabic_article']}", "image": url}
        print("PAYLOAD:", payload)
        return {"status":"printed", "payload": payload}
