class ProcessedNews:
    def __init__(self, content_hash, normalized_text, source_chat_id, message_id):
        self.content_hash = content_hash
        self.normalized_text = normalized_text
        self.source_chat_id = source_chat_id
        self.message_id = message_id
