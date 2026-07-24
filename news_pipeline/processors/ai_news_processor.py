import asyncio, json, logging
logger = logging.getLogger(__name__)
class AINewsProcessor:
    def __init__(self, provider): self.provider = provider
    async def process(self, text, prompt=None):
        result = await self.provider.process_message(text, prompt=prompt)
        print("\n========== RAW MODEL RESPONSE ==========")
        print(result)
        print("========================================\n")
        cleaned = result.strip()
        if cleaned.startswith("```json"): cleaned = cleaned[7:]
        if cleaned.startswith("```"): cleaned = cleaned[3:]
        if cleaned.endswith("```"): cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
        print("========== CLEANED RESPONSE ==========")
        print(cleaned)
        print("======================================\n")
        try:
            parsed = json.loads(cleaned)
        except Exception:
            print("========== JSON PARSE FAILED ==========")
            print("Raw response:")
            print(result)
            print("=======================================\n")
            logger.exception("JSON parse failed")
            raise ValueError(f"Model did not return valid JSON.\n\nResponse:\n{result}")
        assert all(k in parsed for k in ("headline_1","arabic_article","image_prompt_en"))
        return parsed
