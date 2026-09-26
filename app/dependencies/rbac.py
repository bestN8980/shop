from fastapi import FastAPI, HTTPException, Depends, Request
from app.core.enums import UserRole
from app.dependencies.auth import get_current_user
from app.modules.users.model import User

#closure + DI
def require_role(allowed_roles: list[UserRole]): #create config
    def checker(current_user: User = Depends(get_current_user)): #runtime logic
        if current_user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="You do not have permission")
        return current_user
    return checker

