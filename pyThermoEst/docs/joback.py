# import libs
import logging
from typing import List, Tuple
# locals
from ..models import JobackGroupContributions

# NOTE: logger
logger = logging.getLogger(__name__)



def joback_group_contribution_info() -> Tuple[List[str],List[str]]:
    """
    Get the list of Joback group contribution.

    Returns
    -------
    Tuple[List[str],List[str]]
        A tuple containing two lists: field names and their corresponding aliases.
    """
    try:
        # NOTE: ids
        group_ids = []
        group_names = []

        # NOTE: alias
        for filed_name, field_info in JobackGroupContributions.model_fields.items():
            # get alias
            alias = field_info.alias

            # >> store alias
            if alias is not None:
                group_ids.append(alias)

            # >> also store field names
            group_names.append(filed_name)

        return group_names, group_ids
    except Exception as e:
        logger.error(f"Error retrieving Joback group contribution IDs: {e}")
        return [], []

def joback_group_contribution_names() -> List[str]:
    """
    Get the list of Joback group contribution names.

    Returns
    -------
    List[str]
        A list of Joback group contribution IDs.
    """
    try:
        # NOTE: keys
        group_ids = list(JobackGroupContributions.model_fields.keys())
        return group_ids
    except Exception as e:
        logger.error(f"Error retrieving Joback group contribution IDs: {e}")
        return []

def joback_group_contribution_ids() -> List[str]:
    """
    Get the list of Joback group contribution IDs.

    Returns
    -------
    List[str]
        A list of Joback group contribution IDs.
    """
    try:
        # NOTE: ids
        _, group_ids = joback_group_contribution_info()

        return group_ids
    except Exception as e:
        logger.error(f"Error retrieving Joback group contribution IDs: {e}")
        return []