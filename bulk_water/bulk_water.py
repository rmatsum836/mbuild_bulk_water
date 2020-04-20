"""
Primary function of recipe here
"""

import mbuild as mb
from mbuild_bulk_water.utils import utils

class build_water_box(mb.Compound, n_compounds, forcefield='spce'):
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
    def __init__(self):
        super(build_water_box, self).__init__()
        # Build a box of water
        water = utils.get_water()
        water_box = mb.fill_box(water, n_compounds, density=1000)

        # Type water system
        ff = utils.get_ff(utils.get_ff_path(forcefield))

        water_PM = ff.apply(water_box)

        return water_PM
