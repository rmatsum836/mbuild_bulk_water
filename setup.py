from setuptools import setup


setup(
    # Self-descriptive entries which should always be present
    name='bulk_water',
    author='Ray Matsumoto',
    author_email='ray.a.matsumoto@vanderbilt.edu',
    license='MIT',
    version='0.0.0',
    description='Build a box of water with mBuild and foyer',
    zip_safe=False,
    entry_points={
        'mbuild.plugins':[
        "build_water_box = bulk_water.bulk_water:build_water_box"
        ]
        }
    )
