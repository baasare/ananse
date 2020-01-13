from setuptools import setup


with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


__project__ = "ananse"
__version__ = "0.0.1"
__description__ = "A python package to partially automate search term selection and writing search strategies for systematic reviews"
__long_description__ = long_description
__long_description_content_type__ = "text/markdown"
__packages__ = ["ananse"]
__author__ = "Bernard Atiemo Asare, Amma Frimpomaa Frimpong-Boateng"
__author_email__ = "asarebernard98@gmail.com, Ammafrimps123@gmail.com"
__requires__ = [
         'numpy',
         'pandas',
         'nltk',
         'rake_nltk',
         'matplotlib',
         'sklearn',
         'scipy',
         'networkx'
         ]
__classifiers__ = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
]


setup(
    name = __project__,
    version = __version__,
    description = __description__,
    long_description=__long_description__,
    long_description_content_type=__long_description_content_type__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    classifiers = __classifiers__,
    requires = __requires__,
)