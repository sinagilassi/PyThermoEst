# import libs
import pyThermoEst
from pyThermoEst.docs.joback import (
    joback_group_contribution_info,
    joback_group_contribution_names,
    joback_group_contribution_ids,
    joback_group_contribution_category
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

# NOTE: get Joback group contribution category
group_category = joback_group_contribution_category()
print(group_category)
print(f"Total categories: {len(group_category)}")
# each group length
for cat, items in group_category.items():
    print(f"Category: {cat}, Total items: {len(items)}")
