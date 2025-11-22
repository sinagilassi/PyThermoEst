# import libs
from pyThermoEst import joback
from pyThermoEst.models import JobackGroupContributions, GroupUnit

import pydantic
print(pydantic.__version__)

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

payload = {
    "-CH3": GroupUnit(value=10.5),
    "-CH2-": GroupUnit(value=8.2),
    ">CH-": GroupUnit(value=0),
}

groups = JobackGroupContributions(**payload)


group2 = JobackGroupContributions(
    methyl=GroupUnit(value=10.5),
    methylene=GroupUnit(value=8.2),
)
