"""
Unit and regression test for the bulk_water package.
"""

# Import package, test suite, and other packages as needed
import bulk_water
import pytest
import sys
import mbuild as mb

def test_bulk_water_imported():
    """ Sample test, will always pass so long as import statement worked """
    assert "bulk_water" in sys.modules

def test_import():
    """ Test that mBuild recipe import works """
    assert "build_water_box" in vars(mb.recipes).keys()
