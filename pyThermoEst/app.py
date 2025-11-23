# import libs
import logging
from typing import Dict
# locals
from .models import JobackGroupContributions
from .core import Joback

# NOTE: logger
logger = logging.getLogger(__name__)


# SECTION: Joback Group Contributions

def joback_calc(groups: JobackGroupContributions | Dict[str, float]):
    """
    Using Joback method to calculate thermodynamic properties including

    Parameters
    ----------
    groups : JobackGroupContributions | Dict[str, float]
        Group contributions for Joback method.

    Returns
    -------

    """
    try:
        # SECTION: initialize Joback method
        Joback_ = Joback(group_contributions=groups)

        # NOTE: group contributions
        groups_ = Joback_.group_contribution_idx

        # SECTION: check group contributions
        valid_groups_ = Joback_._check_group_contributions()

        return groups_, valid_groups_
    except Exception as e:
        logger.error(f"Error in Joback calculation: {e}")
        return None
