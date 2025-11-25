# import libs
import logging
from typing import Dict, Optional
# locals
from .models import (
    JobackGroupContributions,
    ZabranskyRuzickaGroupContributions,
    ZabranskyRuzickaGroupContributionsCorrections
)
from .core import Joback, ZabranskyRuzicka


# NOTE: logger
logger = logging.getLogger(__name__)


# SECTION: Joback Group Contributions

def joback_calc(
    groups: JobackGroupContributions | Dict[str, float],
    total_atoms_number: int
):
    """
    Using Joback method to calculate thermodynamic properties including

    Parameters
    ----------
    groups : JobackGroupContributions | Dict[str, float]
        Group contributions for Joback method.
    total_atoms_number : int
        Total number of atoms in the molecule.

    Returns
    -------
    dict
        Calculated thermodynamic properties.

    Notes
    -----
    You can use either the field names or their aliases to specify group contributions. For example:
    - methyl has alias '-CH3'
    - methylene has alias '-CH2- @non-ring'
    - imine_non_ring has alias '-N= @non-ring'
    - imine_ring has alias '-N= @ring'

    """
    try:
        # SECTION: initialize Joback method
        Joback_ = Joback(
            group_contributions=groups,
            total_atoms_number=total_atoms_number
        )

        # NOTE: calculate properties
        return Joback_._calc()
    except Exception as e:
        logger.error(f"Error in Joback calculation: {e}")
        return None

# SECTION: Zabransky-Ruzicka Group Contributions


def zabransky_ruzicka_calc(
    group_contributions: ZabranskyRuzickaGroupContributions | Dict[str, float],
    group_corrections: Optional[
        ZabranskyRuzickaGroupContributionsCorrections | Dict[str, float]
    ] = None
):
    """
    Using Zabransky-Ruzicka method to calculate thermodynamic properties including

    Parameters
    ----------
    group_contributions : ZabranskyRuzickaGroupContributions | Dict[str, float]
        Group contributions for Zabransky-Ruzicka method.
    group_corrections : Optional[ZabranskyRuzickaGroupContributionsCorrections | Dict[str, float]]
        Group correction contributions for Zabransky-Ruzicka method.

    Returns
    -------
    dict
        A dictionary containing calculated thermodynamic properties as:
        - value: equation to calculate heat capacity (Cp_LIQ).
        - units: units of the heat capacity (J/mol).
        - symbol: symbol representing heat capacity (Cp_LIQ).

    Notes
    -----
    You can use either the field names or their aliases to specify group contributions. For example:
    - methyl has alias '-CH3'
    - methylene has alias '-CH2- @non-ring'
    - imine_non_ring has alias '-N= @non-ring'
    - imine_ring has alias '-N= @ring'

    """
    try:
        # SECTION: initialize Zabransky-Ruzicka method
        ZabranskyRuzicka_ = ZabranskyRuzicka(
            group_contributions=group_contributions,
            group_corrections=group_corrections
        )

        # NOTE: calculate properties
        return ZabranskyRuzicka_._calc()
    except Exception as e:
        logger.error(f"Error in Zabransky-Ruzicka calculation: {e}")
        return None
