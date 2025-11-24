# import libs
from typing import Optional, Dict
from pydantic import BaseModel, Field, ConfigDict
# local
from .ref import GroupUnit

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
        alias="-CH2- @non-ring"
    )
    tertiary_CH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Tertiary CH group contribution.",
        alias=">CH- @non-ring"
    )
    quaternary_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Quaternary C group contribution.",
        alias=">C< @non-ring"
    )
    vinyl_CH2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl CH2 group contribution.",
        alias="=CH2"
    )
    vinyl_CH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl CH group contribution.",
        alias="=CH- @non-ring"
    )
    vinyl_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl C group contribution.",
        alias="=C< @non-ring"
    )
    allene: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Allene group contribution.",
        alias="=C="
    )
    alkyne_CH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Alkyne CH group contribution.",
        alias="#CH"
    )
    alkyne_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Alkyne C group contribution.",
        alias="#C-"
    )
    methylene_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Methylene group contribution in ring.",
        alias="-CH2- @ring"
    )
    tertiary_CH_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Tertiary CH group contribution in ring.",
        alias=">CH- @ring"
    )
    quaternary_C_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Quaternary C group contribution in ring.",
        alias=">C< @ring"
    )
    vinyl_CH_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl CH group contribution in ring.",
        alias="=CH- @ring"
    )
    vinyl_C_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Vinyl C group contribution in ring.",
        alias="=C< @ring"
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
    ether_non_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Ether O (non-ring) group contribution.",
        alias="-O- @non-ring"
    )
    ether_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Ether O (ring) group contribution.",
        alias="-O- @ring"
    )
    carbonyl_non_ring: Optional[GroupUnit] = Field(
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
    secondary_amine_non_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Secondary amine >NH (non-ring) group contribution.",
        alias=">NH @non-ring"
    )
    secondary_amine_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Secondary amine >NH (ring) group contribution.",
        alias=">NH @ring"
    )
    tertiary_amine_non_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Tertiary amine >N- (non-ring) group contribution.",
        alias=">N- @non-ring"
    )
    imine_non_ring: Optional[GroupUnit] = Field(
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
    thioether_non_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Thioether -S- (non-ring) group contribution.",
        alias="-S- @non-ring"
    )
    thioether_ring: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        description="Thioether -S- (ring) group contribution.",
        alias="-S- @ring"
    )


class JobackGroupData(BaseModel):
    """A class to represent a Joback group with its name and contribution data."""
    id: str
    name: str
    count: float
    data: Dict[str, str]


class JobackHeatCapacity(BaseModel):
    a: float = Field(..., description="Cp correlation parameter a")
    b: float = Field(..., description="Cp correlation parameter b")
    c: float = Field(..., description="Cp correlation parameter c")
    d: float = Field(..., description="Cp correlation parameter d")

    # optional: make parameters immutable after creation
    model_config = ConfigDict(frozen=True)

    def __call__(self, T: float) -> float:
        """
        Evaluate Cp at temperature T (K).
        """
        return (
            self.a - 37.93 +
            (self.b + 0.210) * T +
            (self.c - 3.91e-4) * T**2 +
            (self.d + 2.06e-7) * T**3
        )

    def Cp(self, T: float) -> float:
        """
        Alias method if you prefer Cp(T) instead of obj(T).
        """
        return self(T)
