import sys, os
print("PYTHON:", sys.executable)
try:
    import dotenv; dotenv.load_dotenv()
except Exception as e:
    import traceback; traceback.print_exc()
try:
    import asyncio
    from news_pipeline.pipeline.news_pipeline import NewsPipeline
    async def main():
        p = NewsPipeline()
        print(await p.run("Sample news"))
    asyncio.run(main())
except Exception as e:
    import traceback
    traceback.print_exc()
