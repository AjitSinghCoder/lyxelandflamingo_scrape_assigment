from typing import Dict, List
from pydantic import BaseModel, HttpUrl


class ScrapeRequest(BaseModel):
    url: HttpUrl

class ScrapeResponse(BaseModel):
    request_id: str

class ResultResponse(BaseModel):
    status: str
    data: List[Dict[str, str]]

class LogEntry(BaseModel):
    request_id: str
    timestamp: str
    status: str

class LogsResponse(BaseModel):
    data: List[LogEntry]

