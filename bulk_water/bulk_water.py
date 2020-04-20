"""
Primary function of recipe here
"""

import mbuild as mb
import os
from pkg_resources import resource_filename

class build_water_box(mb.Compound):
    """
    Example class that would go in your recipe.

    Parameters
    ----------
    n_compounds : int
        Number of water molecules in the box
    forcefield : str, optional, default='spce'
        Name of force field to parametrize water

    Returns
    -------
    water_PM : Parametrized ParmEd structure
        ParmEd structure of a box of water
    """
    def __init__(self, n_compounds=1000, forcefield='spce'):
        super(build_water_box, self).__init__()
        # Build a box of water
        water = _get_water()
        water_box = mb.fill_box(water, n_compounds, density=1000)

        # Type water system
        ff = _get_ff(_get_ff_path(forcefield))

        water_PM = ff.apply(water_box)

        return water_PM

def _get_water():
    cache_dir = resource_filename('mbuild_bulk_water', 'lib')
    filename = 'water.mol2'
    water = mb.load(os.path.join(cache_dir, filename))
    water.name = 'SOL'

    return water

def _get_ff_path(ff_name):
    """Get the path to a force field xml file """
    """in a directory of the same name."""
    ff_path = resource_filename('mbuild_bulk_water',
                                os.path.join('lib', ff_name + '.xml'))
    return ff_path

def _get_ff(ff_name):
    """Get the Forcefield object from a force field xml file """
    """in a directory of the same name."""
    ff_name = ff_name.lower()
    ff_path = get_ff_path(ff_name)
    FF = Forcefield(ff_path)
    return FF
