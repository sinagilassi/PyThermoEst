# import libs
from pydantic import BaseModel, Field

# NOTE: Quantity


class GroupUnit(BaseModel):
    """A class to represent a physical quantity with a value and unit."""
    value: float = Field(
        0,
        description="The numerical value of the quantity."
    )
