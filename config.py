from pydantic import BaseModel


class Settings(BaseModel):
    api_key: str
    url: str


settings = Settings(api_key='48a90ac42caa09f90dcaeee4096b9e53', url='http://api.openweathermap.org/data/2.5/weather?q=')