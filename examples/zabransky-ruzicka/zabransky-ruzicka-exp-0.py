# import libs
import pyThermoEst
from pyThermoEst.docs.zabransky_ruzicka import (
    zabransky_ruzicka_group_contribution_info,
    zabransky_ruzicka_group_contribution_names,
    zabransky_ruzicka_group_contribution_ids,
    zabransky_ruzicka_group_correction_info,
    zabransky_ruzicka_group_correction_ids,
    zabransky_ruzicka_group_correction_names
)
from rich import print

# version
print(f"pyThermoEst version: {pyThermoEst.__version__}")

# SECTION: get Zabransky-Ruzicka group contribution info
group_info = zabransky_ruzicka_group_contribution_info()
print(group_info)

# SECTION: get Zabransky-Ruzicka group contribution names
group_names = zabransky_ruzicka_group_contribution_names()
print(group_names)

# SECTION: get Zabransky-Ruzicka group contribution IDs
group_ids = zabransky_ruzicka_group_contribution_ids()
print(group_ids)

# SECTION: get Zabransky-Ruzicka group correction info
correction_info = zabransky_ruzicka_group_correction_info()
print(correction_info)

# SECTION: get Zabransky-Ruzicka group correction names
correction_names = zabransky_ruzicka_group_correction_names()
print(correction_names)

# SECTION: get Zabransky-Ruzicka group correction IDs
correction_ids = zabransky_ruzicka_group_correction_ids()
print(correction_ids)
