from ananse import Ananse


def main():
    min_len = 1  # minimum keyword length
    max_len = 4  # maximum keyword length

    # Create an instance of the package
    test_run = Ananse()

    # Import your naive search results from the current working directory
    imports = test_run.import_naive_results(path="./")

    # Columns to deduplicate imported search results
    columns = ['title', 'abstract']

    # De-duplicate the imported search results
    data = test_run.deduplicate_dataframe(imports, columns)

    # Extract keywords from article title and abstract as well as author and database tagged keywords
    all_terms = test_run.extract_terms(data, min_len=min_len, max_len=max_len)

    # Create Document-Term Matrix, with columns as terms and rows as articles
    dtm, term_column = test_run.create_dtm(data.text, keywords=all_terms, min_len=max_len, max_len=max_len)

    # Create co-occurrence network using Document-Term Matrix
    graph_network = test_run.create_network(dtm, all_terms)

    # Plot histogram and node strength of the network
    test_run.plot_degree_histogram(graph_network)
    test_run.plot_degree_distribution(graph_network)

    # Determine cutoff for the relevant keywords
    cutoff_strengths = test_run.find_cutoff(graph_network, "spline", "degree", degrees=3, knot_num=1, percent=0.879956,
                                            diagnostics=True)

    # Get suggested keywords and save to a csv file
    suggested_keywords = test_run.get_keywords(graph_network, "degree", cutoff_strengths, save_keywords=True)

    # Print suggested keywords
    for word in suggested_keywords:
        print(word)


if __name__ == '__main__':
    main()
