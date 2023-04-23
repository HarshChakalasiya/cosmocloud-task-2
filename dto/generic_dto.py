from typing import Optional, List

from util.base_model import BaseModel


class ResponseState(BaseModel):
    status_code: int = 0
    error_message: Optional[str] = None


class SearchResult(BaseModel):
    total: int = 0
    records: List = []