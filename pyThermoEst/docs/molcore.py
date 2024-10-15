# MOLE CORE

# import packages/modules
import os
import yaml


# local


class MolCore:
    def __init__(self):
        pass

    def load_yml_ref(self, reference_name):
        '''
        Loads YAML reference file.

        Parameters
        ----------
        reference_name : str
            Name of the reference file.

        Returns
        -------
        ref_dict : dict
            Dictionary of the reference file.
        '''
        try:
            # load reference file
            # current file path
            current_path = os.path.dirname(os.path.abspath(__file__))
            # parent path
            parent_path = os.path.abspath(os.path.join(current_path))
            # reference path
            reference_path = os.path.join(
                parent_path, 'reference', reference_name)
            # load reference file
            with open(reference_path, 'r') as f:
                ref_dict = yaml.safe_load(f)
            # return reference dictionary
            return ref_dict
        except Exception as e:
            raise Exception("Loading reference failed!, ", e)
