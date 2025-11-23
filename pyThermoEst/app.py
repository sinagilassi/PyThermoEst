# import libs
import logging
from typing import Dict, Literal
# locals
from .models import JobackGroupContributions
from .core import Joback

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
