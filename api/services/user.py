import os
import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from decouple import config

security = HTTPBasic()


class UserService:

    @classmethod
    def get_current_username(cls, credentials: HTTPBasicCredentials = Depends(security)) -> str:
        """
        validates credentials of current user based in this simple case environment variables based.
        :param credentials: credentials instance
        :return: validated username, else raise authorization error
        """
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = bytes(os.environ.get("USER"), "utf-8)")
        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )
        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = bytes(os.environ.get("PASSWORD"), "utf-8)")
        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
