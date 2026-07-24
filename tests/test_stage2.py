from news_pipeline.models.processed_news import ProcessedNews
assert ProcessedNews("abc","txt",1,2).content_hash == "abc"
print("Stage 2 tests passed")
