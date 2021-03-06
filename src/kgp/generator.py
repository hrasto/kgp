import sys
from .kgp import main

def generate(grammar: str = 'kant'):
    """[summary]

    Args:
        grammar (str): Path to an xml describing a grammar or one of 'kant', 'thanks', 'husserl', 'russiansample', 'reclamation'. Default value is 'kant'.

    Returns:
        str: generated text
    """
    return main(['-g', grammar])