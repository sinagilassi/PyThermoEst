# import libs
import pyThermoEst
from pyThermoEst import zabransky_ruzicka_calc
from pyThermoEst.models import (
    ZabranskyRuzickaGroupContributions,
    ZabranskyRuzickaGroupContributionsCorrections,
    GroupUnit
)
from rich import print

# version
print(f"pyThermoEst version: {pyThermoEst.__version__}")

# SECTION: Example Zabransky-Ruzicka Group Contributions Usage
# NOTE: group data
payload = {
    'C-(H)3(C)': GroupUnit(value=2),
    'C-(H)2(C)2': GroupUnit(value=1),
    'C-(H)(C)3': GroupUnit(value=1),
    'C-(H)2(C)(Cd)': GroupUnit(value=2),
    'Cd-(H)2': GroupUnit(value=1),
    'Cd-(H)(C)': GroupUnit(value=1),
    'Cd-(C)2': GroupUnit(value=2),
}

group_data = ZabranskyRuzickaGroupContributions(**payload)
# log
print(group_data)

# NOTE: corrections data
corrections_payload = {
    'Cyclohexene': GroupUnit(value=1),
}

group_corrections = ZabranskyRuzickaGroupContributionsCorrections(
    **corrections_payload)

# log
print(group_corrections)

# SECTION: dimethyl carbonate
payload_dmcarbonate = {
    'C-(H)3(O)': GroupUnit(value=2),
    'CO-(O)2': GroupUnit(value=1),
    'O-(C)(CO)': GroupUnit(value=2),
}
group_data_dmcarbonate = ZabranskyRuzickaGroupContributions(
    **payload_dmcarbonate)


# SECTION: Calculate Zabransky-Ruzicka properties
result = zabransky_ruzicka_calc(
    group_contributions=group_data_dmcarbonate
)
print(result)

# calculate Cp_LIQ at 300 K
if result:
    Cp_LIQ_eq = result['value']
    print(type(Cp_LIQ_eq))
    Cp_LIQ_value = Cp_LIQ_eq(298.15)
    Cp_LIQ_unit = result['unit']
    Cp_LIQ_symbol = result['symbol']
    print(f"Cp_LIQ at 300 K: {Cp_LIQ_value} {Cp_LIQ_unit} ({Cp_LIQ_symbol})")
