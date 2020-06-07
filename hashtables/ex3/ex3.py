def intersection(arrays):
    # create a new dict to store the amount of times each number is used
    counts = dict()

    # traverse each sublist in the input array
    for list in arrays:

        # traverse each number in the sublists
        for num in list:

            # if the current number already exists in the counts dict, increment its count
            # otherwise, set its count to 1 at the current index in the counts dict
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

    # create an empty list to store the intersection numbers
    intersections = []

    # use .items() to create a list of key-value tuples for the numbers and their counts
    for tuple in counts.items():

        # if the current number's count is equal to the length of the input array,
        # add the current number to the intersections list
        if tuple[1] == len(arrays):
            intersections.append(tuple[0])
        else:
            # otherwise, continue the loop
            continue

    # return the list of intersection numbers
    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
