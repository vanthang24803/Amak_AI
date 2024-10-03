from pydantic import BaseModel, Field
from datetime import datetime

class Response(BaseModel):
    message: str
    isSuccess: bool = Field(default=False)
    code: int
    timestamp: datetime = Field(default_factory=datetime.now)

    @classmethod
    def send(cls, code: int, message: str):
        is_success = code == 200
        return cls(message=message, code=code, isSuccess=is_success)
