from pydantic import BaseModel, field_validator


class UserCreate(BaseModel):
    id: int
    username: str | None = None
    email: str | None = None
    password: str | None = None
    firstname: str | None = None
    lastname: str | None = None
    usercol: str | None = None
    character: int
    
    @field_validator('username', 'email', 'firstname', 'lastname', 'usercol')
    def check_string_length(cls, v):
        if v is not None and len(v) > 45:
            raise ValueError('String must be no longer than 45 characters')
        return v
    
class UserGet(BaseModel):
    id: int
    username: str | None = None
    email: str | None = None
    firstname: str | None = None
    lastname: str | None = None
    usercol: str | None = None
    character: int
    
    @field_validator('username', 'email', 'firstname', 'lastname', 'usercol')
    def check_string_length(cls, v):
        if v is not None and len(v) > 45:
            raise ValueError('String must be no longer than 45 characters')
        return v

class UserPut(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    firstname: str | None = None
    lastname: str | None = None
    
    @field_validator('username', 'email', 'firstname', 'lastname')
    def check_string_length(cls, v):
        if v is not None and len(v) > 45:
            raise ValueError('String must be no longer than 45 characters')
        return v