from datetime import datetime
import uuid
from mongoengine import Document, StringField, DateTimeField, ListField, DictField

class ScrapingRequest(Document):
    request_id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    url = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    status = StringField(choices=["pending", "finished"], default="pending")
    data = ListField(DictField(), default=list)
   