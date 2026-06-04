from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB_NAME: str

    SECRET_KEY: str = "DEV-SECRET-KEY-DO-NOT-USE-IN-PRODUCTION"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    BCRYPT_ROUNDS: int = 12

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def mongo_uri(self):
        return self.MONGO_URI

    @property
    def database_name(self):
        return self.MONGO_DB_NAME


settings = Settings()