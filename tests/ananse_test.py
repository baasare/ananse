from ananse import Ananse


def main():
    test_run = Ananse()
    imports = test_run.import_naive_results(path="./")

    data = test_run.deduplicate_dataframe(imports, ['title', 'abstract'])

    all_terms = test_run.extract_terms(data)

    dtm, term_column = test_run.create_dtm(data.text, all_terms)

    dtm_dataframe = test_run.dtm_to_dataframe(dtm, term_column, data.text)
    # print(dtm_dataframe)

    graph_network = test_run.create_network(dtm, all_terms)

    test_run.plot_degree_histogram(graph_network)
    test_run.plot_degree_distribution(graph_network)
    test_run.plot_rank_degree_distribution(graph_network)

    cutoff_strengths = test_run.find_cutoff(graph_network, "spline", "degree")
    suggested_keywords = test_run.get_keywords(graph_network, "degree", cutoff_strengths, save_keywords=True)

    print("Suggested Keywords")
    for suggested_keyword in suggested_keywords:
        print(suggested_keyword)


if __name__ == '__main__':
    main()
