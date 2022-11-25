from pydantic import BaseModel, Field


class UserOutput(BaseModel):
    username: str = Field(description="name of user", example="stan")
