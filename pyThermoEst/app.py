# import libs

# local
from .config import __author__, __description__, __package__, __version__


def main():
    print(f"Author: {__author__}")
    print(f"Package: {__package__}")
    print(f"Description: {__description__}")
    print(f"Version: {__version__}")


def estimate():
    print("This is the estimate function.")
