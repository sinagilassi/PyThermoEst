# 🧪 PyThermoEst

PyThermoEst is a Python toolkit for estimating thermodynamic properties from group-contribution methods. It currently supports the **Joback** method for estimating a wide range of properties and the **Zabransky–Ruzicka** method for predicting the liquid-phase heat capacity.

## 📦 Installation

```bash
pip install pyThermoEst
```

## 🚀 Usage

The package exposes convenience helpers in `pyThermoEst.app` for both calculation workflows. See the `examples/` directory for runnable scripts.

### 🧬 Joback property estimation

Provide Joback group contributions along with the total number of atoms, then call `joback_calc`. You can mix field names or their documented aliases when building `JobackGroupContributions`.

```python
from pyThermoEst import joback_calc
from pyThermoEst.models import JobackGroupContributions, GroupUnit

payload = {
    "-CH3": GroupUnit(value=2),
    "=CH- @ring": GroupUnit(value=3),
    "=C< @ring": GroupUnit(value=3),
    "-OH @phenol": GroupUnit(value=1),
}

joback_groups = JobackGroupContributions(**payload)
result = joback_calc(groups=joback_groups, total_atoms_number=18)

# Evaluate a temperature-dependent property, e.g., heat capacity at 273 K
cp_273 = result["heat_capacity"]["value"](273)
print(cp_273)
```

### 💧 Zabransky–Ruzicka liquid heat capacity

To compute liquid heat capacity, provide required group contributions and optional correction terms, then call `zabransky_ruzicka_calc`.

```python
from pyThermoEst import zabransky_ruzicka_calc
from pyThermoEst.models import (
    ZabranskyRuzickaGroupContributions,
    ZabranskyRuzickaGroupContributionsCorrections,
    GroupUnit,
)

payload = {
    "C-(H)3(O)": GroupUnit(value=2),
    "CO-(O)2": GroupUnit(value=1),
    "O-(C)(CO)": GroupUnit(value=2),
}

contributions = ZabranskyRuzickaGroupContributions(**payload)
corrections = ZabranskyRuzickaGroupContributionsCorrections()

result = zabransky_ruzicka_calc(group_contributions=contributions,
                                group_corrections=corrections)
cp_liq_at_300k = result["value"](298.15)
print(cp_liq_at_300k, result["unit"], result["symbol"])
```

### 📚 Getting group contribution IDs and names

You can inspect available group contribution identifiers and names for each method:

#### 🧬 Joback group contributions

```python
from pyThermoEst.docs.joback import (
    joback_group_contribution_info,
    joback_group_contribution_names,
    joback_group_contribution_ids
)

# Get all group contribution IDs (aliases)
group_ids = joback_group_contribution_ids()

# Get all group contribution names (field names)
group_names = joback_group_contribution_names()

# Get both names and IDs as tuples
names, ids = joback_group_contribution_info()
```

#### 💧 Zabransky–Ruzicka group contributions

```python
from pyThermoEst.docs.zabransky_ruzicka import (
    zabransky_ruzicka_group_contribution_info,
    zabransky_ruzicka_group_contribution_names,
    zabransky_ruzicka_group_contribution_ids,
    zabransky_ruzicka_group_correction_info,
    zabransky_ruzicka_group_correction_ids,
    zabransky_ruzicka_group_correction_names
)

# Get group contribution IDs (aliases)
group_ids = zabransky_ruzicka_group_contribution_ids()

# Get group contribution names (field names)
group_names = zabransky_ruzicka_group_contribution_names()

# Get both names and IDs as tuples
names, ids = zabransky_ruzicka_group_contribution_info()

# Get correction term IDs
correction_ids = zabransky_ruzicka_group_correction_ids()

# Get correction term names
correction_names = zabransky_ruzicka_group_correction_names()

# Get both correction names and IDs as tuples
corr_names, corr_ids = zabransky_ruzicka_group_correction_info()
```

### 📖 Further examples

- `examples/joback-exp-0.py`: Inspect available Joback group IDs and names.
- `examples/joback-exp-1.py`: Build Joback group payloads with field names or aliases.
- `examples/joback-exp-2.py`: Full Joback calculation including temperature evaluation.
- `examples/zabransky-ruzicka-exp-0.py`: Inspect available Zabransky–Ruzicka group IDs, names, and corrections.
- `examples/zabransky-ruzicka-exp-1.py`: Zabransky–Ruzicka calculation with optional corrections.

## 🔧 API reference

- `pyThermoEst.app.joback_calc(groups, total_atoms_number)`: Runs Joback method and returns calculated properties.
- `pyThermoEst.app.zabransky_ruzicka_calc(group_contributions, group_corrections=None)`: Returns an equation for liquid heat capacity plus units and symbol metadata.

Each function accepts either the pydantic models or plain dictionaries keyed by group identifiers; aliases are supported for convenience.
