# import libs
import os
# local
from ..util import SourceLoader


class Core:
    '''
    Core class.
    '''
    def __init__(self):
        # init
        self.SourceLoader = SourceLoader()
        
        # load reference
        self.ref_dict = self.load_ref()
    
    def load_ref(self):
        '''
        Load reference files.
        '''        
        # current file path
        current_path = os.path.dirname(os.path.abspath(__file__))
        # parent path
        parent_path = os.path.abspath(current_path + '/..')
            
        # load reference
        ref_dict = self.SourceLoader.load_yml_ref(
            reference_name='sheet1.yml',
            reference_folder='data',
            current_path=current_path,
            parent_path=parent_path
        )
        # return reference
        return ref_dict