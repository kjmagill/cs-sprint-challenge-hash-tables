def finder(files, queries):
    paths = dict()
    result = []

    # traverse each path in the 'files' input array
    for path in files:

        # since we know that each path stores a filename at the end,
        # we'll split each path at "/" and select the -1 index to grab the filename
        split_up_path = path.split("/")
        path_filename = split_up_path[-1]
        
        # if the current filename is not already in the paths dict,
        # add it to the dict with an intitial value of an empty list
        if path_filename not in paths:
            paths[path_filename] = []
        
        # append the current path to the paths dict
        # with its filename as its key and the current path as its value
        paths[path_filename].append(path)

    # traverse each filename in the 'queries' input array
    for query_filename in queries:

        # if the filename is already in the paths dict, extend the result list
        # by adding the list of paths stored at the current index in the paths dict
        if query_filename in paths:
            result.extend(paths[query_filename])

    # return the list of all paths containing the queried filenames
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
