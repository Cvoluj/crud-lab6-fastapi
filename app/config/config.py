from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    PORT: int
    DB_HOST: str
    DB_PORT: int
    MYSQL_DB: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    @property
    def DB_URL(self):
        return f'mysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@localhost:{self.DB_PORT}/{self.MYSQL_DB}'        

    model_config = SettingsConfigDict(env_file='.env')


server_setting = ServerSettings()