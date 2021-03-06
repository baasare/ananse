# Ananse

This project is a collaboration between Dr. Effah Antwi,Research Scientist, Natural Resources Canada, Canadian Forest Service 
and Dr Wiafe Owusu-Banahene, Department of Computer Engineering, School of Engineering Sciences, University of Ghana, Legon, Accra, Ghana. 
The ``Ananse`` package is a python package  designed to partially automate search term selection and writing search strategies for systematic reviews. Read the documentation at [baasare.github.io/ananse](https://baasare.github.io/ananse/_build/html/index.html) and [ananse.readthedocs.io/](https://ananse.readthedocs.io/en/latest/)

## Setup
Ananse requires python 3.7 or higher


### Using pip

```bash
pip install ananse
```

### Directly from the repository

```bash
git clone https://github.com/baasare/ananse.git
python ananse/setup.py install
```

## Quick start        
### Writing your own script


```python
from ananse import Ananse
    
min_len = 1 # minimum keyword length
max_len = 4 # maximum keyword length


# Create an instance of the package
test_run = Ananse()


# Import your naive search results from the current working directory
imports = test_run.import_naive_results(path="./")

# Columns to deduplicate imported search results
columns =  ['title', 'abstract']


#de-duplicate the imported search results
data = test_run.deduplicate_dataframe(imports, columns)


#extract keywords from article title and abstract as well as author and database tagged keywords
all_terms = test_run.extract_terms(data, min_len=min_len, max_len=max_len)


#create Document-Term Matrix, with columns as terms and rows as articles
dtm, term_column = test_run.create_dtm(data.text, keywords=all_terms, min_len=max_len, max_len=max_len)


#create co-occurrence network using Document-Term Matrix
graph_network = test_run.create_network(dtm, all_terms)


#plot histogram and node strength of the network
test_run.plot_degree_histogram(graph_network)
test_run.plot_degree_distribution(graph_network)


#Determine cutoff for the relevant keywords
cutoff_strengths = test_run.find_cutoff(graph_network, "spline", "degree", degrees=3, knot_num=1, percent=0.879956,
                                            diagnostics=True)


#get suggested keywords and save to a csv file
suggested_keywords = test_run.get_keywords(graph_network, "degree", cutoff_strengths, save_keywords=True)


#Print suggested keywords
for word in suggested_keywords:
   print(word)


```
### Using Ananse Test Script


```bash
python tests/ananse_test
```

## References

This is a python implementation of the R package as mentioned in paper [An automated approach to identifying search terms for systematic reviews using keyword co‐occurrence networks by Eliza M. Grames, Andrew N. Stillman  Morgan W. Tingley and Chris S. Elphick](https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13268)