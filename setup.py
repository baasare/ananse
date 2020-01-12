import os
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
     name='ananse',  
     version='0.1',
     scripts=['ananse'] ,
     author="Bernard Atiemo Asare",
     author_email="asarebernard98@gmail.com",
     keywords = "keyword-extraction NLP",
     description="A python package to partially automate search term selection and writing search strategies for systematic reviews",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/baasare/ananse",
     packages=setuptools.find_packages(),
     setup_requires=[
         'numpy',
         'pandas',
         'nltk',
         'rake_nltk',
         'matplotlib',
         'sklearn',
         'scipy',
         ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )