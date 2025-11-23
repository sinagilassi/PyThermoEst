# import libs
import pyThermoEst
from pyThermoEst.docs.joback import (
    joback_group_contribution_info,
    joback_group_contribution_names,
    joback_group_contribution_ids
    )
from rich import print

# version
print(f"pyThermoEst version: {pyThermoEst.__version__}")

# NOTE: get Joback group contribution IDs
group_info = joback_group_contribution_info()
print(group_info)

# NOTE: get Joback group contribution names
group_names = joback_group_contribution_names()
print(group_names)

# NOTE: get Joback group contribution IDs
group_ids = joback_group_contribution_ids()
print(group_ids)