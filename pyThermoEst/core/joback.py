# import libs
import logging
import os
# locals
from ..util import ReferenceLoader

# NOTE: logger
logger = logging.getLogger(__name__)


class Joback:
    '''
    Joback method implementation.
    '''

    def __init__(self):
        pass

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

            # data file name
            data_name = 'joback.csv'

            # NOTE: load CSV reference
            joback_df = ref_loader.load_csv_ref(
                reference_name=data_name,
                reference_folder=data_folder,
            )

            # return Joback parameters
            return joback_df
        except Exception as e:
            raise Exception("Loading Joback parameters failed!, ", e)
