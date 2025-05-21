from typing import Literal, List, Optional, Dict, Union, Any

from pydantic import BaseModel, Field, model_validator, field_validator


class PeopleModel(BaseModel):
    main_beds: int
    extra_beds: int
    max_adults: int
    min_adults: int

    @field_validator("main_beds", "extra_beds", "max_adults", "min_adults")
    def validate_fields(cls, value) -> int:
        if isinstance(value, str) and value.isdigit():
            return int(value)
        else:
            raise ValueError("Значение должно быть числом")


class ExtraArrayModel(BaseModel):
    beds: Optional[Dict[int, Dict[int, int]]] = {}
    excluded: Optional[str] = None
    set_guests: Optional[int] = None
    people: Optional[PeopleModel] = None
    children_ages: Optional[Dict[str, Any]] = {}

    @field_validator("set_guests")
    def coerce_set_guests(cls, value) -> Optional[int]:
        if value is None:
            return value
        return int(value)


class PhotoModel(BaseModel):
    id: int
    name: str
    file_name: str
    mime_type: str
    size: int
    account_id: int
    create_date: str
    update_date: str
    roomtype_id: int
    order: int
    url: str
    thumb: str


class RoomModel(BaseModel):
    id: int
    parent_id: int
    name: str
    name_ru: str
    name_en: str
    description_ru: str
    description_en: str
    description: str
    adults: int
    children: int
    photos: Optional[List[PhotoModel]] = None
    accommodation_type: Literal[
        0,
        1,
        2,
        3,
        4,
        5,
    ]
    bed_variant: Optional[
        Literal[
            0,
            1,
            2,
            3,
        ]
    ] = None
    amenities: Union[List, Dict[int, Dict]] = []
    extra_array: Optional[ExtraArrayModel] = None

    @field_validator(
        "id",
        "name",
        "description",
        "name_ru",
        "name_en",
        "description_ru",
        "description_en",
    )
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError(f"Пустое поле")
        else:
            return value

    @field_validator("photos")
    def validate_photos(cls, photos):
        if photos is None:
            return photos
        for i, photo in enumerate(photos):
            if not isinstance(photo, PhotoModel):
                raise ValueError(f"Элемент {photo} не является PhotoModel")
            for field_name, value in photo.model_dump().items():
                if value is None:
                    raise ValueError(
                        f"Поле {field_name} в фото {i} не должно быть пустым"
                    )
        return photos


class RoomsModel(BaseModel):
    rooms: List[RoomModel]


if __name__ == "__main__":
    pass
