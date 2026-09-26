from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from app.dependencies.database import get_db
from app.core.security import decode_access_token
from app.modules.users.repository import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login/oauth2"
)

def get_current_user(
    db=Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    user = get_user_by_id(db, int(user_id))

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return user