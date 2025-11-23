# import libs
import logging
from typing import Dict
import os
# locals
from ..models import JobackGroupContributions, GroupUnit
from ..util import ReferenceLoader
from ..config import JOBACK_DATA_FILE, JOBACK_TABLE_COLUMN_GROUP

# NOTE: logger
logger = logging.getLogger(__name__)


class Joback:
    '''
    Joback method implementation.

    - The Joback group contribution method (often called Joback-Reid method) estimates 11 thermodynamic properties of organic compounds, such as boiling point, critical temperature, and heat of formation, by breaking molecules into 41 predefined functional groups and summing their contributions.
    - It assumes no interactions between groups, making it simple but less accurate for complex or aromatic compounds; estimates are generally within 5-15% error for many properties based on tested datasets.
    - To use it, identify and count the functional groups in the molecule (e.g., for ethanol: one -CH₃, one -CH₂-, one -OH @alcohol), then apply the summation formulas for the desired property—research suggests it's most reliable for mid-sized aliphatic organics, with potential inaccuracies for rings or halogens.
    - All 41 groups are categorized into non-ring, ring, halogen, oxygen, nitrogen, and sulfur types, with specific contribution values for each property.
    '''

    def __init__(
        self,
        group_contributions: JobackGroupContributions | Dict[str, float],
    ):
        '''
        Initializes Joback method with group contributions.

        Parameters
        ----------
        group_contributions : JobackGroupContributions | Dict[str, float]
            Group contributions for Joback method.
        '''
        # NOTE: group contributions
        self.group_contributions = group_contributions

        # SECTION: load Joback parameters
        self.joback_params = self.load_joback_parameters()

        # SECTION: get group contribution
        self.group_id = self._get_group_contribution()

    def __repr__(self) -> str:
        return f"""Joback Method with {len(self.group_id)} groups  \n
        Group Contributions: {self.group_contributions} """

    @property
    def group_contribution_idx(self):
        '''
        Returns the group contribution index.

        Returns
        -------
        group_id : dict
            Dictionary of group contributions.
        '''
        return self.group_id

    def load_joback_parameters(
        self,
    ):
        '''
        Loads Joback parameters from reference file.

        Returns
        -------
        joback_params : pd.DataFrame
            DataFrame of Joback parameters.
        '''
        try:
            # load reference file
            ref_loader = ReferenceLoader()

            # current folder
            current_folder = os.path.dirname(os.path.abspath(__file__))
            #  data folder
            data_folder = os.path.join(
                current_folder,
                '..',
                'data',
            )

            # NOTE: load CSV reference
            joback_df = ref_loader.load_csv_ref(
                reference_name=JOBACK_DATA_FILE,
                reference_folder=data_folder,
            )

            # return Joback parameters
            return joback_df
        except Exception as e:
            raise Exception("Loading Joback parameters failed!, ", e)

    def _get_group_contribution(
        self,
    ):
        '''
        Gets group contribution for a specific group.

        Parameters
        ----------
        None

        Returns
        -------
        contribution : dict
            Dictionary of group contributions for various properties.
        '''
        try:
            # filter Joback parameters for the specific group
            group_data = self.joback_params[
                JOBACK_TABLE_COLUMN_GROUP
            ]

            # extract contributions
            contribution = group_data.to_dict()

            return contribution
        except Exception as e:
            raise Exception(f"Getting contribution for group failed!, ", e)

    def list_available_groups(
        self,
    ):
        '''
        Lists all available Joback groups.

        Returns
        -------
        groups : list
            List of available Joback groups.
        '''
        try:
            # get list of available groups
            groups = self.joback_params[JOBACK_TABLE_COLUMN_GROUP].tolist()

            return groups
        except Exception as e:
            raise Exception("Listing available Joback groups failed!, ", e)

    def _get_group_contribution_data(
        self,
        group_name: str,
    ):
        '''
        Gets contribution data for a specific group.

        Parameters
        ----------
        group_name : str
            Name of the group.

        Returns
        -------
        group_data : dict
            Dictionary of contribution data for the group with header names as keys.
        '''
        try:
            # filter Joback parameters for the specific group
            group_data = self.joback_params[
                self.joback_params[JOBACK_TABLE_COLUMN_GROUP] == group_name
            ]

            # convert to Series and then to dictionary with column headers as keys
            return group_data.iloc[0].to_dict() if len(group_data) > 0 else {}
        except Exception as e:
            raise Exception(
                f"Getting contribution data for group {group_name} failed!, ", e)

    def _check_group_contributions(
            self
    ) -> Dict[str, float]:
        """
        Checks the validity of group contributions.
        """
        try:
            # NOTE: count occurrences
            valid_groups = {}

            # count each group
            if isinstance(self.group_contributions, dict):
                # ! dictionary type
                # iterate over group contributions
                for group_name, group_value in self.group_contributions.items():
                    # check if group exists in Joback parameters
                    if group_name in self.group_id.values():
                        # add to count dictionary
                        valid_groups[group_name] = {
                            'count': group_value,
                            'data': self._get_group_contribution_data(group_name)
                        }
            elif isinstance(self.group_contributions, JobackGroupContributions):
                # ! dataclass type
                # iterate over dataclass fields
                for field_name, field_info in JobackGroupContributions.model_fields.items():
                    # get field alias (Joback group name)
                    alias = field_info.alias

                    # check if field is None
                    if alias is None:
                        continue

                    # value stored in the model instance = use field_name
                    group_unit: GroupUnit = getattr(
                        self.group_contributions, field_name)

                    # check if group value is greater than 0
                    if group_unit.value > 0:
                        # check if group exists in Joback parameters
                        if alias in self.group_id.values():
                            # add to count dictionary
                            valid_groups[alias] = {
                                'count': group_unit.value,
                                'data': self._get_group_contribution_data(field_name)
                            }
            else:
                logger.error("Invalid type for group contributions!")
                return valid_groups

            return valid_groups
        except Exception as e:
            raise Exception("Checking group contributions failed!, ", e)
