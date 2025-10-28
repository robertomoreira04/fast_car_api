from typing import Optional
from pydantic import BaseModel

class CarSchema(BaseModel):
    brand: str
    model: str 
    color: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    description: Optional[str] = None

class CarPublic(BaseModel):
    id: int
    brand: str
    model: str 
    color: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    description: Optional[str] = None

class CarList(BaseModel):
    cars: list[CarPublic]