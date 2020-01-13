About this project
==========================
The ``Ananse`` package is a python implementation of the ``litsearchr`` R package  designed to partially automate search term selection and writing search strategies for systematic reviews.

Preparing a Search Strategy for a Systematic Review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Report by:
--------------------------------------------------------

• Bernard Atiemo Asare

• Amma Frimpomaa Frimpong-Boateng

Writing the Naïve Search and Importing the Results:
--------------------------------------------------------

[1]When writing a naive search, the first step is to clearly articulate
the research question. This serves as the basis for identifying concept
groups and naive search terms. Using naïve search, a Boolean search was
performed to return significant articles. The naive search entails
relevant search terms grouped into concept categories, or sets of
synonymous terms. With our project we grouped the search terms into four
concept categories and then combine them into a Boolean search. If
imprecision of the naïve search is high, irrelevant keywords would be
identified. This imprecision may also strain the keyword selection
process leading to the selection of unnecessary and vague terms.

Assembling and deduplicating results
------------------------------------

In searching for information many articles having similar contents may
pop up from multiple databases with some appearing more than once. Naïve
search results need to be assembled and deduplicated to prevent this
over-representation. Due to the different formats in the exportation
results from databases this manual process takes more time. For our
project we considered two databases; Web of science with a .csv file
extension and Scopus with a .txt file extension. Provided the path to
the directory of search results is given, the **import\_naive\_results**
function automatically finds the database and file type of each file,
selects analogous columns and joins them to form a single dataset. This
function imports the search results from a specified path. If the
parameters ``clean_dataset`` and ``save_dataset`` are set to true, then the
function de-duplicates search results after importing and saves the full
search results to a .csv respectively. The parameter ``save_directory``
contains the path to a directory where search results will be saved if
``save_dataset`` is set to TRUE while the parameter path takes the path
containing the naive search results files. After the results are
obtained a pandas data frame consisting of assembled search results is
returned. 

Keyword Extraction
------------------------------------

Extracting and Identifying Keywords [2]Rapid Automatic
Keyword Extraction (RAKE) is a well-known keyword extraction method
which uses a list of stopwords and phrase delimiters to detect the most
relevant words or phrases in a piece of text. The function
**extract\_terms** terms calls the RAKE algorithm and eliminates
keywords that only appear in a single article, and excludes phrases with
only one word from the list of potential keywords resulting in a more
precise search. Then with our method, the author- and database-tagged
keywords are combined with the search terms.


Co-occurrence Network 
------------------------------------

The author tagged and database tagged keywords are combined as dictionary
object created with**extract\_terms** to define all possible keywords.
All the possible keywords are then passed to the function **create\_dtm**.
[3]Then there is a generation of a keyword cooccurrence network where each node
represents a potential search term and the edges arc co-occurrences of
two terms in the title, abstract, or tagged keywords of a study, with
the function **create\_network** which measures the importance of each
term in relation to the selected topic being reviewed. Node strength, a
weighted measure of the degrees of a network that indicates how
well-connected a node is to other strong nodes is the default attribute
used by litsearchr is the measure of node importance. The function
**get\_centrality** is used to rank nodes by strength and using genetic
algorithm finds knots since there are regions of rapid change where
nodes become increasingly more important due to the fact that the node
strength of a network tends to follow a power law.

Identifying Important nodes using the full network
--------------------------------------------------

There are two methods to identify important nodes in the litsearchr
package:

1)Fitting a spline model to the node importance to select tipping points

2)Finding the minimum number of nodes to capture a large percent of the
total importance of the network.(Cumulative Approach)

Depending on the distribution and preference one can decide which method
to use. In choosing a method the first thing to do is to look at the
distribution of node importance. The distribution can be plotted with the
function **plot\_degree\_distribution**, **plot\_rank\_degree\_distribution** or 
**plot\_degree\_histogram**

A spline model for finding cutoff is an appropriate method to identify the 
cutoff threshold for keyword importance if the rank distribution plot has 
a lot of fairly weak nodes with a long tail.The cumulative approach is more 
appropriate when there are no clear breaks in the data.

The **find\_cutoff** function finds the cutoff for a graph network using
either cumulative or spline method of cutting of the degree
distribution. Then the **reduce\_graph** function generates a graph
consisting of only important nodes after which the **get\_keyword**
function extract the keywords from the reduced network.

For this project, the databases supported were mainly Web
Of Science and Scopus.

[1]E. Stillman, "Introduction to litsearchr with an example of writing a
systematic review search strategy for black-backed woodpecker occupancy
of post-fire forest systems", Elizagrames.github.io, 2020. [Online].
Available:
https://elizagrames.github.io/litsearchr/introduction\_vignette\_v010.html.
[Accessed: 08- Jan- 2020].

[2]"Keyword Extraction", MonkeyLearn, 2020. [Online]. Available:
https://monkeylearn.com/keyword-extraction/. [Accessed: 08- Jan- 2020].

[3]2020. [Online]. Available:
https://www.researchgate.net/publication/220365325\_Mapping\_knowledge\_structure\_by\_keyword\_co-occurrence\_A\_first\_look\_at\_journal\_papers\_in\_Technology\_Foresight.
[Accessed: 08- Jan- 2020].
