# TOOLS
# ----------------------
# import libs
import os
import yaml


class SourceLoader:
    '''
    Used to load reference files.
    '''
    def __init__(self):
        pass
    
    def load_yml_ref(self, reference_name, reference_folder, current_path, parent_path):
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
            # reference path
            reference_path = os.path.join(
                parent_path, reference_folder, reference_name)
            # load reference file
            with open(reference_path, 'r') as f:
                ref_dict = yaml.safe_load(f)
            # return reference dictionary
            return ref_dict
        except Exception as e:
            raise Exception("Loading reference failed!, ", e)
