from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str 
    REDIS_URL: str 
    SMTP_SERVER: str
    SMTP_PORT: int 
    SMTP_USERNAME: str 
    SMTP_PASSWORD: str 
    EMAIL_FROM: str 
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int
    class Config:
        env_file = '.env'

settings = Settings()