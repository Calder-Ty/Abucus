try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description':'A personal Finance tool for budgeting and goal setting',

    'author': 'Tyler Calder',

    'url': 'https://github.com/Calder-Ty/Abucus',

    'download_url' : 'https://github.com/Calder-Ty/Abucus',

    'version' : '0.1',

    'install_requires' :['nose'],

    'packages' : ['Abacus', 'decimal'],

    'scripts': [],

    'name': 'Abacus'

    }

setup(**config)