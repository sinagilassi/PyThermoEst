# import libs
# import libs
from typing import Optional, Dict
from pydantic import BaseModel, Field, ConfigDict
# local
from .ref import GroupUnit

# SECTION: Zabransky-Ruzicka Group Contributions


class ZabranskyRuzickaGroupContributions(BaseModel):
    """Zabransky-Ruzicka group contribution identifiers and their corresponding contributions to thermodynamic properties."""
    model_config = ConfigDict(populate_by_name=True, extra='forbid')

    C_H_3_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0),
        alias="C-(H)3(C)"
    )
    C_H_2_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(C)2")
    C_H_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(C)3")
    C_C_4: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(C)4")
    CD_H_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cd-(H)2")
    CD_H_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cd-(H)(C)")
    CD_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cd-(C)2")
    CD_H_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cd-(H)(Cd)")
    CD_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cd-(C)(Cd)")
    C_H_2_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(C)(Cd)")
    C_H_2_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(Cd)2")
    C_H_C_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(C)2(Cd)")
    C_C_3_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(C)3(Cd)")
    CT_H: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct-(H)")
    CT_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct-(C)")
    CT_CB: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct-(CB)")
    CA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ca")
    CB_H: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CB-(H)")
    CB_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CB-(C)")
    CB_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CB-(Cd)")
    C_H_2_OH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(OH)")
    C_H_OH_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)2")
    C_OH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)3")
    C_H_2_O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(O)")
    C_H_O_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(O)(C)")
    C_H_O_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(O)(Cd)")
    C_O_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(C)2")
    C_O_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(C)(Cd)")
    C_O_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(Cd)2")
    C_H_2_O_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(O)2")
    C_H_O_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(O)2(C)")
    C_H_O_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(O)2(Cd)")
    C_O_2_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)2(C)2")
    C_O_2_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)2(C)(Cd)")
    C_O_2_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)2(Cd)2")
    C_H_OOH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OOH)")
    C_O_COOH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(COOH)")
    C_H_2_HAL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(Hal)")
    C_H_HAL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(Hal)2")
    C_HAL_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)3")
    C_H_2_NH_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(NH2)")
    C_H_NH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NH2)(C)")
    C_H_NH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NH2)(Cd)")
    C_NH_2_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NH2)(C)2")
    C_NH_2_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NH2)(C)(Cd)")
    C_NH_2_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NH2)(Cd)2")
    C_H_2_NH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(NH)")
    C_H_NH_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NH)(C)")
    C_H_NH_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NH)(Cd)")
    C_NH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NH)(C)2")
    C_NH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NH)(C)(Cd)")
    C_NH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NH)(Cd)2")
    C_H_2_CN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CN)")
    C_H_CN_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(CN)(C)")
    C_H_CN_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(CN)(Cd)")
    C_CN_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(CN)(C)2")
    C_CN_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(CN)(C)(Cd)")
    C_CN_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(CN)(Cd)2")
    C_H_2_NO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(NO2)")
    C_H_NO_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NO2)(C)")
    C_H_NO_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NO2)(Cd)")
    C_NO_2_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(C)2")
    C_NO_2_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(C)(Cd)")
    C_NO_2_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(Cd)2")
    C_H_2_NCO: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(NCO)")
    C_H_NCO_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NCO)(C)")
    C_H_NCO_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NCO)(Cd)")
    C_NCO_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NCO)(C)2")
    C_NCO_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NCO)(C)(Cd)")
    C_NCO_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NCO)(Cd)2")
    C_H_2_NCS: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(NCS)")
    C_H_NCS_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NCS)(C)")
    C_H_NCS_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(NCS)(Cd)")
    C_NCS_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NCS)(C)2")
    C_NCS_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NCS)(C)(Cd)")
    C_NCS_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NCS)(Cd)2")
    C_H_2_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CH3)")
    C_H_2_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CH2)(C)")
    C_H_2_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CH2)(Cd)")
    C_H_2_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CH)(C)2")
    C_H_2_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CH)(C)(Cd)")
    C_H_2_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(CH)(Cd)2")
    C_H_2_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(C)3")
    C_H_OH_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(CH3)")
    C_H_OH_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(CH2)(C)")
    C_H_OH_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(CH2)(Cd)")
    C_H_OH_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(CH)(C)2")
    C_H_OH_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(CH)(C)(Cd)")
    C_H_OH_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(CH)(Cd)2")
    C_H_OH_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(OH)(C)3")
    C_OH_CH_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)2")
    C_OH_CH_3_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)(CH2)(C)")
    C_OH_CH_3_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)(CH2)(Cd)")
    C_OH_CH_3_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)(CH)(C)2")
    C_OH_CH_3_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)(CH)(C)(Cd)")
    C_OH_CH_3_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)(CH)(Cd)2")
    C_OH_CH_3_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH3)(C)3")
    C_OH_CH_2_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH2)(C)2")
    C_OH_CH_2_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH2)(C)(Cd)")
    C_OH_CH_2_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH2)(Cd)2")
    C_OH_CH_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH)(C)3")
    C_OH_CH_C_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH)(C)2(Cd)")
    C_OH_CH_C_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH)(C)(Cd)2")
    C_OH_CH_CD_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(CH)(Cd)3")
    C_OH_C_4: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(OH)(C)4")
    C_O_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)")
    C_O_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH2)(C)")
    C_O_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH2)(Cd)")
    C_O_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(C)2")
    C_O_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(C)(Cd)")
    C_O_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(Cd)2")
    C_O_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(C)3")
    C_O_CH_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)2")
    C_O_CH_3_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)(CH2)(C)")
    C_O_CH_3_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)(CH2)(Cd)")
    C_O_CH_3_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)(CH)(C)2")
    C_O_CH_3_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)(CH)(C)(Cd)")
    C_O_CH_3_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)(CH)(Cd)2")
    C_O_CH_3_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH3)(C)3")
    C_O_CH_2_C_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH2)(C)2")
    C_O_CH_2_C_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH2)(C)(Cd)")
    C_O_CH_2_CD_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH2)(Cd)2")
    C_O_CH_C_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(C)3")
    C_O_CH_C_2_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(C)2(Cd)")
    C_O_CH_C_CD_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(C)(Cd)2")
    C_O_CH_CD_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(CH)(Cd)3")
    C_O_C_4_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)(C)4")
    C_HAL_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(CH3)")
    C_HAL_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(CH2)(C)")
    C_HAL_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(CH2)(Cd)")
    C_HAL_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(CH)(C)2")
    C_HAL_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(CH)(C)(Cd)")
    C_HAL_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(CH)(Cd)2")
    C_HAL_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Hal)(C)3")
    C_NO_2_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(CH3)")
    C_NO_2_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(CH2)(C)")
    C_NO_2_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(CH2)(Cd)")
    C_NO_2_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(CH)(C)2")
    C_NO_2_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(CH)(C)(Cd)")
    C_NO_2_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(CH)(Cd)2")
    C_NO_2_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(NO2)(C)3")
    CH_3_O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)")
    CH_3_O_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(CH3)")
    CH_3_O_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(CH2)(C)")
    CH_3_O_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(CH2)(Cd)")
    CH_3_O_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(CH)(C)2")
    CH_3_O_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(CH)(C)(Cd)")
    CH_3_O_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(CH)(Cd)2")
    CH_3_O_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)(C)3")
    CH_3_O_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2")
    CH_3_O_2_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(CH3)")
    CH_3_O_2_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(CH2)(C)")
    CH_3_O_2_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(CH2)(Cd)")
    CH_3_O_2_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(CH)(C)2")
    CH_3_O_2_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(CH)(C)(Cd)")
    CH_3_O_2_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(CH)(Cd)2")
    CH_3_O_2_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(O)2(C)3")
    CH_3_HAL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(Hal)")
    CH_3_HAL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(Hal)2")
    CH_3_HAL_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(Hal)3")
    CH_3_NO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NO2)")
    CH_3_NO_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NO2)2")
    CH_3_NO_2_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NO2)3")
    CH_3_CN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(CN)")
    CH_3_NCS: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NCS)")
    CH_3_NH_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NH2)")
    CH_3_NH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NH-)")
    CH_3_N: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)")
    CH_3_NH_2_O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NH2)(O)")
    CH_3_NH_2_O_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NH2)(O)2")
    CH_3_NH_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NH)(CH3)")
    CH_3_NH_CH_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NH)(CH3)2")
    CH_3_N_CH_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH3)2")
    CH_3_N_CH_3_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH3)3")
    CH_3_N_CH_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH2)(C)")
    CH_3_N_CH_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH2)(Cd)")
    CH_3_N_CH_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH)(C)2")
    CH_3_N_CH_C_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH)(C)(Cd)")
    CH_3_N_CH_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(CH)(Cd)2")
    CH_3_N_C_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(N<)(C)3")
    CH_3_S: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(S)")
    CH_3_S_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(S)2")
    CH_3_S_CH_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(S)(CH3)")
    CH_3_S_CH_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(S)(CH3)2")
    CH_3_NCO: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-(NCO)")
    CH_2_O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">CH2(>O)")
    CH_2_CN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">CH2(>CN)")
    CH_2_NO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">CH2(>NO2)")
    CH_2_HAL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">CH2(>Hal)")
    CH_2_S: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">CH2(>S)")
    CCL_4: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl4")
    CCL_3_CL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl3-Cl")
    CCL_3_F: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl3-F")
    CCL_3_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl3-Br")
    CCL_3_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl3-I")
    CCL_2_F_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl2F2")
    CCL_2_CL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl2Cl2")
    CCL_2_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl2Br2")
    CCL_2_I_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CCl2I2")
    CCL_F_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CClF3")
    CCL_BR_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CClBr3")
    CCL_I_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CClI3")
    CF_4: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CF4")
    CHCL_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHCl3")
    CHCL_2_CL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHCl2-Cl")
    CHCL_2_F: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHCl2-F")
    CHCL_2_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHCl2-Br")
    CHCL_2_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHCl2-I")
    CHCL_2_OH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHCl2-OH")
    CHCL_F_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHClF2")
    CHCL_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHClBr2")
    CHCL_I_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHClI2")
    CHF_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHF3")
    CHBR_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHBr3")
    CHI_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHI3")
    CH_2_CL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2Cl2")
    CH_2_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2Br2")
    CH_2_I_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2I2")
    CH_2_CL_F: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2ClF")
    CH_2_CL_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2ClBr")
    CH_2_CL_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2ClI")
    CH_2_F_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2FBr")
    CH_2_F_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2FI")
    CH_2_BR_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH2BrI")
    CH_3_CL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-Cl")
    CH_3_CF_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CF3")
    CH_3_CCL_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CCl3")
    CH_3_CBR_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CBr3")
    CH_3_CI_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CI3")
    CH_3_CCL_F: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CClF")
    CH_3_CCL_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CClBr")
    CH_3_CCL_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CClI")
    CH_3_CF_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFBr")
    CH_3_CF_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFI")
    CH_3_CBR_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CBrI")
    CH_3_CCL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CCl2")
    CH_3_CF_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CF2")
    CH_3_CB_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CB2")
    CH_3_CI_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CI2")
    CH_3_CF_2_CL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CF2Cl")
    CH_3_CF_2_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CF2Br")
    CH_3_CF_2_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CF2I")
    CH_3_CCL_2_F: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CCl2F")
    CH_3_CCL_2_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CCl2Br")
    CH_3_CCL_2_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CCl2I")
    CH_3_CF_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFBr2")
    CH_3_CF_I_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFI2")
    CH_3_CCL_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CClBr2")
    CH_3_CCL_I_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CClI2")
    CH_3_CF_CL_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFClBr")
    CH_3_CF_CL_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFClI")
    CH_3_CF_BR_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CFBrI")
    CH_3_CCL_BR_I: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH3-CClBrI")
    CH_4: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CH4")
    CN_H: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CN-(H)")
    CHO: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CHO")
    C_H_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)3")
    C_H_2_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(C)")
    C_H_C_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(C)2")
    C_C_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(C)3")
    C_H_2_CD: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)2(Cd)")
    C_H_CD_C: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(Cd)(C)")
    C_CD_C_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Cd)(C)2")
    C_H_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(H)(Cd)2")
    C_C_CD_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(C)(Cd)2")
    C_CD_3_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(Cd)3")
    C_4: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C<4")
    CT: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct")
    CT_C_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct-(C)2")
    CT_CB_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct-(CB)2")
    CT_C_CB: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ct-(C)(CB)")
    CA_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ca2")
    CA_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ca3")
    CB: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CB")
    C_N: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C<-(N)")
    C_N_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C<-(N)2")
    C_N_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C<-(N)3")
    CS_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CS2")
    CS: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CS<")
    C_O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)")
    C_O_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)2")
    C_S_N: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(S)(N)")
    C_S_N_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(S)(N)2")
    CO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CO2")
    CS_2_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="CS2<")
    C_O_O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="C-(O)-O")
    G_1_2_O_CL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,2-O-Cl2")
    G_1_2_O_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,2-O-Br2")
    G_1_1_O_CL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,1-O-Cl2")
    G_1_1_O_BR_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,1-O-Br2")
    G_1_2_O_CL_BR: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,2-O-ClBr")
    G_1_2_O_CL_F: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,2-O-ClF")
    G_1_3_O_CL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,3-O-Cl2")
    O: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">O")
    NH: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">NH")
    NH_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">NH2")
    NCL_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="NCl3")
    N: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">N<")
    NS: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">NS")
    NS_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">NS2")
    NU: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">N-")
    S: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias=">S-")
    SO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="SO2")
    NO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="NO2")
    NO_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="NO3")
    HO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="HO2")
    HOSO_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="HOSO2")
    HAL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="-(Hal)")
    S_CL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="S-Cl")
    S_CL_2: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="S-Cl2")
    S_CCL_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="S-CCl3")
    S_CB_3: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="S-CB3")
    G_1_3_BENZENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,3-benzene")
    G_1_4_BENZENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,4-benzene")
    G_1_2_BENZENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,2-benzene")


class ZabranskyRuzickaGroupContributionsCorrections(BaseModel):
    """Zabransky-Ruzicka group contribution correction identifiers and their corresponding corrections to thermodynamic properties."""
    model_config = ConfigDict(populate_by_name=True, extra='forbid')

    CYCLOPROPANEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclopropanea")
    CYCLOBUTANE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclobutane")
    CYCLOPENTANE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclopentane")
    CYCLOHEXANE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclohexane")
    CYCLOHEPTANEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cycloheptanea")
    CYCLOOCTANEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclooctanea")
    CYCLOPENTENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclopentene")
    CYCLOHEXENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclohexene")
    CYCLOHEXADIENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cyclohexadiene")
    INDAN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Indan")
    G_1H_INDENEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1H-indenea")
    HEXAHYDROINDAN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Hexahydroindan")
    TETRALIN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Tetralin")
    HEXAHYDRONAPHTHALENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Hexahydronaphthalene")
    OCTAHYDRO_1H_INDENEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Octahydro-1H-indenea")
    NAPHTHALENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Naphthalene")
    BIPHENYL: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Biphenyl")
    ANTHRACENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Anthracene")
    PHENANTHRENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Phenanthrene")
    PYRENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Pyrene")
    G_1H_FLUORENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1H-fluorene")
    ADAMANTANE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Adamantane")
    HEXAMETHYLENETETRAMINE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Hexamethylenetetramine")
    DECAHYDRONAPHTHALENE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Decahydronaphthalene")
    ETHYLENEOXIDE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ethyleneoxide")
    G_1_3_DIOXOLANE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="1,3-Dioxolane")
    FURAN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Furan")
    TETRAHYDROFURAN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Tetrahydrofuran")
    TETRAHYDROPYRAN: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Tetrahydropyran")
    PYRROLIDINE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Pyrrolidine")
    PIPERIDINE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Piperidine")
    THIACYCLOBUTANEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Thiacyclobutanea")
    THIACYCLOPENTANE: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Thiacyclopentane")
    THIACYCLOHEXANEA: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Thiacyclohexanea")
    CIS: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Cis-")
    TRANS: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Trans-")
    ORTHO: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Ortho-")
    META: Optional[GroupUnit] = Field(
        default_factory=lambda: GroupUnit(value=0), alias="Meta-")
