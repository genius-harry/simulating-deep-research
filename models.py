from pydantic import BaseModel
from typing import List, Optional

class SearchQuery(BaseModel):
    search_terms: List[str]

class DecisionOutput(BaseModel):
    should_continue: bool
    new_search_terms: Optional[List[str]]
    final_answer: Optional[str]
    sources: Optional[List[str]]