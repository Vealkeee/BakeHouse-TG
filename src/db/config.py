from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PW: str
    DB_PORT: int
    DB_USER: str

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()