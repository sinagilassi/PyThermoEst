# import libs
import logging
from typing import Dict, Any
from math import pow
import os
# locals
from ..models import (
    GroupUnit,
    ZabranskyRuzickaGroupContributions,
    ZabranskyRuzickaGroupContributionsCorrections,
    ZabranskyRuzickaGroupData
)
from ..util import ReferenceLoader
from ..configs import (
    ZABRANSKY_RUZICKA_DATA_FILE_1,
    ZABRANSKY_RUZICKA_DATA_FILE_2,
    ZABRANSKY_RUZICKA_TABLE_COLUMN_GROUP,
    ZABRANSKY_RUZICKA_REFERENCE
)

# NOTE: logger
logger = logging.getLogger(__name__)


class ZabranskyRuzicka:
    '''
    Zabransky-Ruzicka method to estimate thermodynamic properties.
    '''

    def __init__(
        self,
        group_contributions: ZabranskyRuzickaGroupContributions | Dict[str, float],
        group_corrections: ZabranskyRuzickaGroupContributionsCorrections | Dict[
            str, float] | None
    ):
        '''
        Initializes the Zabransky-Ruzicka method.

        Parameters
        ----------
        group_contributions : ZabranskyRuzickaGroupContributions | Dict[str, float]
            Group contributions for the compound.
        group_corrections : ZabranskyRuzickaGroupContributionsCorrections | Dict[
            str, float] | None
            Group corrections for the compound.
        '''
        # NOTE: group contributions
        self.group_contributions = group_contributions
        self.group_corrections = group_corrections

        # SECTION: load parameters
        self.params, self.corrections = self.load_parameters()

        # SECTION: get group contribution
        self.group_id = self._get_group_contribution()

        # SECTION: valid groups
        self.valid_group_contribution = self._check_group_contributions(
            group_contributions)
        self.valid_group_corrections = self._check_group_contributions(
            group_corrections) if group_corrections is not None else {}

        # >> merge valid groups
        self.valid_groups = {
            **self.valid_group_contribution,
            **self.valid_group_corrections
        }

    def __repr__(self) -> str:
        return f"""Zabransky Ruzicka Method: \n
        Group Contributions: {self.group_contributions} \n
        Group Corrections: {self.group_corrections}  \n
        Reference: {ZABRANSKY_RUZICKA_REFERENCE}
        """

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

    def load_parameters(
        self,
    ):
        '''
        Loads parameters from reference file.

        Returns
        -------
        params_df, corrections_df : pd.DataFrame, pd.DataFrame
            DataFrames of parameters and corrections.
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
            params_df = ref_loader.load_csv_ref(
                reference_name=ZABRANSKY_RUZICKA_DATA_FILE_1,
                reference_folder=data_folder,
            )

            # NOTE: corrections
            corrections_df = ref_loader.load_csv_ref(
                reference_name=ZABRANSKY_RUZICKA_DATA_FILE_2,
                reference_folder=data_folder,
            )

            # return parameters dataframe
            return params_df, corrections_df
        except Exception as e:
            raise Exception("Loading  parameters failed!, ", e)

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
            # filter  parameters for the specific group
            group_data = self.params[
                ZABRANSKY_RUZICKA_TABLE_COLUMN_GROUP
            ]

            # extract contributions
            contribution = group_data.to_dict()

            return contribution
        except Exception as e:
            raise Exception(f"Getting contribution for group failed!, ", e)

    def _get_correction_contribution(
        self,
    ):
        '''
        Gets correction contribution for a specific group.

        Parameters
        ----------
        None

        Returns
        -------
        contribution : dict
            Dictionary of correction contributions for various properties.
        '''
        try:
            # filter  corrections for the specific group
            correction_data = self.corrections[
                ZABRANSKY_RUZICKA_TABLE_COLUMN_GROUP
            ]

            # extract contributions
            contribution = correction_data.to_dict()

            return contribution
        except Exception as e:
            raise Exception(
                f"Getting correction contribution for group failed!, ", e)

    def list_available_groups(
        self,
    ):
        '''
        Lists all available  groups.

        Returns
        -------
        groups : list
            List of available  groups.
        '''
        try:
            # get list of available groups
            groups = self.params[ZABRANSKY_RUZICKA_TABLE_COLUMN_GROUP].tolist()

            return groups
        except Exception as e:
            raise Exception("Listing available  groups failed!, ", e)

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
            # filter  parameters for the specific group
            group_data = self.params[
                self.params[ZABRANSKY_RUZICKA_TABLE_COLUMN_GROUP] == group_name.strip(
                )
            ]

            # convert to Series and then to dictionary with column headers as keys
            return group_data.iloc[0].to_dict() if len(group_data) > 0 else {}
        except Exception as e:
            raise Exception(
                f"Getting contribution data for group {group_name} failed!, ", e)

    def _check_group_contributions(
            self,
            group_data: Dict[str, Any] | ZabranskyRuzickaGroupContributions |
        ZabranskyRuzickaGroupContributionsCorrections
    ) -> Dict[str, ZabranskyRuzickaGroupData]:
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
                    # check if group exists in  parameters
                    if group_name in self.group_id.values():
                        # add to count dictionary
                        res_ = ZabranskyRuzickaGroupData(
                            id=group_name,
                            name=group_name,
                            count=float(group_value),
                            data=self._get_group_contribution_data(group_name)
                        )
                        # append
                        valid_groups[group_name] = res_
            elif isinstance(
                self.group_contributions, (
                    ZabranskyRuzickaGroupContributions,
                    ZabranskyRuzickaGroupContributionsCorrections
                )
            ):
                # ! dataclass type
                # iterate over dataclass fields
                for field_name, field_info in ZabranskyRuzickaGroupContributions.model_fields.items():
                    # get field alias ( group name)
                    alias = field_info.alias

                    # check if field is None
                    if alias is None:
                        continue

                    # value stored in the model instance = use field_name
                    group_unit: GroupUnit = getattr(
                        self.group_contributions,
                        field_name
                    )

                    # check if group value is greater than 0
                    if group_unit.value > 0:
                        # check if group exists in  parameters
                        if alias in self.group_id.values():
                            # add to count dictionary
                            res_ = ZabranskyRuzickaGroupData(
                                id=alias,
                                name=field_name,
                                count=float(group_unit.value),
                                data=self._get_group_contribution_data(alias)
                            )
                            # append
                            valid_groups[alias] = res_

            else:
                logger.error("Invalid type for group contributions!")
                return valid_groups

            return valid_groups
        except Exception as e:
            raise Exception("Checking group contributions failed!, ", e)

    def _calc_sigma(
            self
    ):
        '''
        Calculates sigma for all valid groups.

        '''
        try:
            # SECTION: calculate sigma
            # initialize critical temperature
            sigma = {
                'a[i]': 0.0,
                'b[i]': 0.0,
                'c[i]': 0.0,
            }

            # iterate over valid groups
            for group_name, group_info in self.valid_groups.items():
                # get group count
                group_count = group_info.count
                # get contribution data
                contribution_data = group_info.data
                # get contribution
                val_a_i = contribution_data.get('a[i]', None)
                val_b_i = contribution_data.get('b[i]', None)
                val_c_i = contribution_data.get('c[i]', None)

                # check if contribution is valid
                if (
                    val_a_i is not None and
                    val_b_i is not None and
                    val_c_i is not None
                ):
                    # calculate sigma contributions
                    sigma['a[i]'] += group_count * float(val_a_i)
                    sigma['b[i]'] += group_count * float(val_b_i)
                    sigma['c[i]'] += group_count * float(val_c_i)

            return sigma
        except Exception as e:
            raise Exception("Calculating critical temperature failed!, ", e)

    def _calc(
            self
    ):
        '''
        Calculates properties using  method.

        Returns
        -------
        properties : dict
            Dictionary of calculated properties.
        '''
        try:
            # SECTION: calculate properties
            properties = {
            }

            # SECTION: calculate sigma
            sigma = self._calc_sigma()

            return properties
        except Exception as e:
            raise Exception("Calculating properties failed!, ", e)
