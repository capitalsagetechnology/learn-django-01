from enum import Enum


class StatusEnum(Enum):
    Active = 'Active'
    Inactive = 'Inactive'


STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)
