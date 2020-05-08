def finder(files, queries):

    """
    YOUR CODE HERE
    """
    q_dict = {}
    result = []
    # for query in queries:
    #     q_dict[query] = None
    for file in files:
        last = file.split("/")[-1]
        if last in q_dict:
            q_dict[last].append(file)
        else:
            q_dict[last] = [file]
    for query in queries:
        if query in q_dict:
            for file in q_dict[query]:
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
