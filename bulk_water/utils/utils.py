import os
from pkg_resources import resource_filename

from foyer import Forcefield
import mbuild as mb

def get_ff_path(ff_name):
    """Get the path to a force field xml file """
    """in a directory of the same name."""
    ff_path = resource_filename('mbuild_bulk_water',
                                os.path.join('lib', ff_name + '.xml'))
    return ff_path

def get_ff(ff_name):
    """Get the Forcefield object from a force field xml file """
    """in a directory of the same name."""
    ff_name = ff_name.lower()
    ff_path = get_ff_path(ff_name)
    FF = Forcefield(ff_path)
    return FF

def get_water():
    cache_dir = resource_filename('mbuild_bulk_water', 'lib')
    filename = 'water.mol2'
    water = mb.load(os.path.join(cache_dir, filename))
    water.name = 'SOL'
    return water
