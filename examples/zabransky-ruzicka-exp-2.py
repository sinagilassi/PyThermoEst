# import libs
import pyThermoEst
from pyThermoEst import zabransky_ruzicka_calc
from rich import print

# version
print(f"pyThermoEst version: {pyThermoEst.__version__}")

# SECTION: Example Zabransky-Ruzicka Group Contributions Usage
# NOTE: group data
group_data = {
    'C-(H)3(C)': 2,
    'C-(H)2(C)2': 1,
    'C-(H)(C)3': 1,
    'C-(H)2(C)(Cd)': 2,
    'Cd-(H)2': 1,
    'Cd-(H)(C)': 1,
    'Cd-(C)2': 2,
}
# log
print(group_data)

# NOTE: corrections data
group_corrections = {
    'Cyclohexene': 1,
}
# log
print(group_corrections)

# SECTION: dimethyl carbonate
group_data_dmcarbonate = {
    'C-(H)3(O)': 2,
    'CO-(O)2': 1,
    'O-(C)(CO)': 2,
}
# log
print(group_data_dmcarbonate)


# SECTION: Calculate Zabransky-Ruzicka properties
result = zabransky_ruzicka_calc(
    group_contributions=group_data_dmcarbonate
)
print(result)

# calculate Cp_LIQ at 300 K
if result:
    Cp_LIQ_eq = result['value']
    print(type(Cp_LIQ_eq))
    Cp_LIQ_value = Cp_LIQ_eq(298.15) if callable(Cp_LIQ_eq) else Cp_LIQ_eq
    Cp_LIQ_unit = result['unit']
    Cp_LIQ_symbol = result['symbol']
    print(f"Cp_LIQ at 300 K: {Cp_LIQ_value} {Cp_LIQ_unit} ({Cp_LIQ_symbol})")
