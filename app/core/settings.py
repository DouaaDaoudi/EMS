from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "ems_db"
    MONGO_TEST_DB_NAME: str = "ems_test_db"

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()