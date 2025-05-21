from pydantic import BaseModel
from typing import Optional, Literal, List, Dict


class ChildrenAgeModel(BaseModel):
    id: int
    min_age: int
    max_age: int
    beds_types: List[Literal[0, 1, 2]]


class AccountDataModel(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    address: str
    address_eng: str
    country: str
    city: str
    city_eng: str
    checkin: str
    checkout: str
    timezone: str
    uid: str
    language: str
    geo_data: str
    hotel_type: Literal[
        "hotel",
        "apartments",
        "hostel",
        "pension",
        "recreational center",
        "sanatorium",
        "apart_hotel",
        "glamping",
        "country_hotel",
        "motel",
        "children_health_camp",
        "other",
    ]
    min_children_age: int
    children_ages: Dict[str, ChildrenAgeModel]


class AccountModel(BaseModel):
    account: AccountDataModel


if __name__ == "__main__":
    pass
