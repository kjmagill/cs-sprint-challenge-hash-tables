def get_indices_of_item_weights(weights, length, limit):
    n = len(weights)
    unmatched_weights = dict()

    # traverse through each of the input weights
    for i in range(n):

        current_weight = weights[i]

        # if the current weight is not already in the unmatched_weights dict, add it
        if current_weight not in unmatched_weights:
            unmatched_weights[current_weight] = i

        counter_weight = limit - current_weight

        # if the counter weight is already in the unmatched_weights dict
        # and its value in the dict is not i...
        if counter_weight in unmatched_weights and unmatched_weights[counter_weight] is not i:
            counter_weight = unmatched_weights[counter_weight]

            # if i is greater than or equal to the counter weight, return [i, counter_weight]
            if i >= counter_weight:
                return [i, counter_weight]
            # if the counter weight is greater than i, return [unmatched_weights[counter_weight], i]
            else:
                return [unmatched_weights[counter_weight], i]

    # if we do not hit any of the above return statements, thus determining
    # that such a pair does not exist for the given input weights, return None
    return None
