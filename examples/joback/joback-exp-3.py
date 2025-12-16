# import libs
import pyThermoEst
from pyThermoEst import joback_heat_capacity_calc, joback_prop_calc
from pyThermoEst.models import JobackGroupContributions, GroupUnit
from rich import print

# version
print(f"pyThermoEst version: {pyThermoEst.__version__}")

# SECTION: Example Joback Group Contributions Usage
# NOTE: group data
payload = {
    "-CH3": GroupUnit(value=2),
    "=CH- @ring": GroupUnit(value=3),
    "=C< @ring": GroupUnit(value=3),
    "-OH @phenol": GroupUnit(value=1),
}

groups = JobackGroupContributions(**payload)
# log
print(groups)
print(groups.methyl)
print(groups.model_dump(by_alias=True))


# NOTE: payload with field names
payload = {
    "methyl": GroupUnit(value=2),
    "vinyl_CH_ring": GroupUnit(value=3),
    "vinyl_C_ring": GroupUnit(value=3),
    "phenol_OH": GroupUnit(value=1),
}
groups = JobackGroupContributions(**payload)
# log
print(groups)

# NOTE: use dictionary format
groups = {
    "-CH3": 2,
    "=CH- @ring": 3,
    "=C< @ring": 3,
    "-OH @phenol": 1,
}

# SECTION: Calculate Joback properties
result = joback_prop_calc(
    groups=groups,
    total_atoms_number=18,
)
print(result)


# SECTION: Calculate Joback heat capacity equation
result = joback_heat_capacity_calc(
    groups=groups,
    total_atoms_number=18,
)
print(result)

if result:
    res_ = result["value"](300) if callable(result["value"]) else None
    print(f"Heat capacity at 300 K: {res_} {result['unit']}")
