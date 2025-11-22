# import libs
# local
from .docs import Core
from .models import JobackGroupContributions


def estimate():
    print("This is the estimate function.")
    CoreC = Core()
    print(CoreC.ref_dict)

# SECTION: Joback Group Contributions


def joback(groups: JobackGroupContributions):
    print("This is the Joback groups function.")
    print(groups)
