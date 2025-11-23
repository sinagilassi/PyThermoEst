# import libs
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

# NOTE: Quantity


class GroupUnit(BaseModel):
    """A class to represent a physical quantity with a value and unit."""
    value: float = Field(
        0,
        description="The numerical value of the quantity."
    )

# SECTION: Joback Group Contributions


class JobackGroupContributions(BaseModel):
    """Joback group contribution identifiers and their corresponding contributions to thermodynamic properties."""
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

    methyl: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Methyl group contribution.",
        alias="-CH3"
    )
    methylene: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Methylene group contribution.",
        alias="-CH2-"
    )
    tertiary_CH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Tertiary CH group contribution.",
        alias=">CH-"
    )
    quaternary_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Quaternary C group contribution.",
        alias=">C<"
    )
    vinyl_CH2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl CH2 group contribution.",
        alias="=CH2"
    )
    vinyl_CH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl CH group contribution.",
        alias="=C-"
    )
    vinyl_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl C group contribution.",
        alias="=C<"
    )
    allene: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Allene group contribution.",
        alias="=C="
    )
    alkyne_CH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Alkyne CH group contribution.",
        alias="≡CH"
    )
    alkyne_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Alkyne C group contribution.",
        alias="≡C-"
    )
    fluorine: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Fluorine group contribution.",
        alias="-F"
    )
    chlorine: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Chlorine group contribution.",
        alias="-Cl"
    )
    bromine: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Bromine group contribution.",
        alias="-Br"
    )
    iodine: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Iodine group contribution.",
        alias="-I"
    )
    alcohol_OH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Alcohol OH group contribution.",
        alias="-OH @alcohol"
    )
    phenol_OH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Phenol OH group contribution.",
        alias="-OH @phenol"
    )
    ether_nonring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Ether O (non-ring) group contribution.",
        alias="-O- @non-ring"
    )
    ether_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Ether O (ring) group contribution.",
        alias="-O- @ring"
    )
    carbonyl_nonring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Carbonyl C=O (non-ring) group contribution.",
        alias=">C=O @non-ring"
    )
    carbonyl_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Carbonyl C=O (ring) group contribution.",
        alias=">C=O @ring"
    )
    aldehyde: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Aldehyde O=CH- group contribution.",
        alias="O=CH-"
    )
    carboxylic_acid: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Carboxylic acid COOH group contribution.",
        alias="-COOH"
    )
    ester: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Ester COO- group contribution.",
        alias="-COO-"
    )
    carbonyl_other: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Carbonyl =O (other) group contribution.",
        alias="=O @expect as above"
    )
    primary_amine: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Primary amine NH2 group contribution.",
        alias="-NH2"
    )
    secondary_amine_nonring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Secondary amine >NH (non-ring) group contribution.",
        alias=">NH @non-ring"
    )
    secondary_amine_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Secondary amine >NH (ring) group contribution.",
        alias=">NH @ring"
    )
    tertiary_amine_nonring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Tertiary amine >N- (non-ring) group contribution.",
        alias=">N- @non-ring"
    )
    imine_nonring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Imine -N= (non-ring) group contribution.",
        alias="-N= @non-ring"
    )
    imine_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Imine -N= (ring) group contribution.",
        alias="-N= @ring"
    )
    imine_secondary: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Secondary imine =NH group contribution.",
        alias="=NH"
    )
    nitrile: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Nitrile CN group contribution.",
        alias="-CN"
    )
    nitro: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Nitro NO2 group contribution.",
        alias="-NO2"
    )
    thiol: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Thiol SH group contribution.",
        alias="-SH"
    )
    thioether_nonring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Thioether -S- (non-ring) group contribution.",
        alias="-S- @non-ring"
    )
    thioether_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Thioether -S- (ring) group contribution.",
        alias="-S- @ring"
    )
