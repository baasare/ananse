import os
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
     name='ananse',  
     version='1.0',
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
         'numpy==1.18.0',
         'pandas==0.25.3',
         'nltk==3.4.5',
         'rake-nltk==1.0.4',
         'matplotlib==3.1.2',
         'scikit-learn==0.22',
         'scipy==1.4.1',
         'networkx==2.4'
         ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )