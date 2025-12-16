# import libs
import pyThermoEst
from pyThermoEst import joback_calc
from pyThermoEst.models import JobackGroupContributions, GroupUnit
from rich import print

# version
print(f"pyThermoEst version: {pyThermoEst.__version__}")

# SECTION: Example Joback Group Contributions Usage
# NOTE: group data
payload = {
    "methyl": GroupUnit(value=10.5),
    "methylene": GroupUnit(value=8.2),
    "tertiary_CH": GroupUnit(value=0),
}

contributions = JobackGroupContributions(
    **payload
)
# log
print(contributions)

payload = {
    "-CH3": GroupUnit(value=10.5),
    "-CH2-": GroupUnit(value=8.2),
    ">CH-": GroupUnit(value=0),
}

groups = JobackGroupContributions(**payload)
# log
print(groups)
print(groups.methyl)
print(groups.model_dump(by_alias=True))

