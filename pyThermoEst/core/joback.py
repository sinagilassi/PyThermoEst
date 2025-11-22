# import libs
import logging
import os
# locals
from ..models import JobackGroupContributions
from ..util import ReferenceLoader
from ..config import JOBACK_DATA_FILE

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
            group_contributions: JobackGroupContributions
    ):
        '''
        Initializes Joback method with group contributions.

        Parameters
        ----------
        group_contributions : JobackGroupContributions
            Group contributions for Joback method.
        '''
        # NOTE: group contributions
        self.group_contributions = group_contributions

        # NOTE: load Joback parameters
        self.joback_params = self.load_joback_parameters()

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
