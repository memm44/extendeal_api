from fastapi import APIRouter, Depends

from app.api.schemas.user.output_user import UserOutput
from app.api.services.user import UserService

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/users/me",response_model=UserOutput)
def read_current_user(username: str = Depends(UserService.get_current_username)):
    return {"username": username}
