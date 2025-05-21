from typing import Literal, Union, List, Optional

from pydantic import BaseModel, field_validator, model_validator


class PlanCancellationModel(BaseModel):
    id: int
    plan_id: int
    date_from: str
    date_to: str
    deadline: int
    fine: Literal[1, 2, 3, 4, 5]
    fine_amount: Union[int, float]


class PlanModel(BaseModel):
    id: int
    name: str
    default: Literal[0, 1]
    description: str
    enabled: Literal[0, 1]
    enabled_ota: Literal[0, 1]
    booking_guarantee_sum: float
    booking_guarantee_unit: Literal["percentage", "absolute"]
    booking_guarantee_link: str
    booking_guarantee_percentage_from: Literal["all", "first_day"]
    booking_guarantee_till: Literal[0, 1]
    booking_guarantee_till_days: int  # 0-1095 guarantee till 1
    booking_guarantee_till_hours: int  # 0-23 guarantee till 1
    booking_guarantee_till_condition: Literal[0, 1, 2]
    booking_guarantee_auto_booking_cancel: Literal[0, 1]  # if guarantee till 1
    cancellation_rule: Literal[0, 1]
    cancellation_rules: str
    restriction_plan_id: int
    nutrition: int  # ???
    board_from_services: Literal[0, 1]
    additional_services_ids: object
    order: int
    legal_entity_id: int
    for_promo_code: Literal[0, 1]
    warranty_type: Literal["no", "onlinepay", "card_warranty"]
    name_ru: str
    name_en: str
    description_ru: str
    description_en: str
    cancellation_rules_ru: str
    cancellation_rules_en: str
    cancellation_deadline: str
    cancellation_fine_type: int
    cancellation_fine_amount: Union[int, float]  # if fine_type 2 - float, else int
    plan_cancellations: List[PlanCancellationModel]

    @model_validator(mode="after")
    def validate_cancellation_fine_amount(self):
        if self.cancellation_fine_type == 2:
            if not isinstance(self.cancellation_fine_amount, float):
                raise ValueError(
                    "cancellation_fine_amount должен быть float, если cancellation_fine_type == 2 (проценты)"
                )
        else:
            if not isinstance(self.cancellation_fine_amount, int):
                raise ValueError(
                    "cancellation_fine_amount должен быть int, если cancellation_fine_type != 2"
                )
        return self

    @field_validator("cancellation_fine_type")
    def validate_cancellation_fine_type(cls, value):
        if isinstance(value, str):
            if value.isdigit():
                value = int(value)
            else:
                raise ValueError("Значение должно быть числом")
        if value not in {1, 2, 3, 4, 5}:
            raise ValueError("Значение должно быть одним из: 1, 2, 3, 4, 5")
        return value

    @field_validator(
        "id",
        "name",
        "description",
        "cancellation_rules",
        "cancellation_rules_ru",
        "cancellation_rules_en",
        "cancellation_deadline",
        "name_ru",
        "name_en",
        "description_ru",
        "description_en",
    )
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError(f"Поле не должно быть пустым")
        else:
            return value

    @model_validator(mode="after")
    def validate_guarantee_fields(self):
        if self.booking_guarantee_till == 1:
            if not (0 <= self.booking_guarantee_till_days <= 1095):
                raise ValueError(
                    "booking_guarantee_till_days должен быть от 0 до 1095, если booking_guarantee_till = 1"
                )
            if not (0 <= self.booking_guarantee_till_hours <= 23):
                raise ValueError(
                    "booking_guarantee_till_hours должен быть от 0 до 23, если booking_guarantee_till = 1"
                )
            if self.booking_guarantee_till_condition not in [0, 1, 2]:
                raise ValueError(
                    "booking_guarantee_till_condition должен быть 0, 1 или 2, если booking_guarantee_till = 1"
                )
            if self.booking_guarantee_auto_booking_cancel not in [0, 1]:
                raise ValueError(
                    "booking_guarantee_auto_booking_cancel должен быть 0 или 1, если booking_guarantee_till = 1"
                )
        return self


class PlansModel(BaseModel):
    plans: List[PlanModel]


if __name__ == "__main__":
    pass
