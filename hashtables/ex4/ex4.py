def has_negatives(a):
    nums = dict()
    result = []

    # traverse each number in the input array
    for num in a:

        # start by adding each number to the nums dict with a value of 1
        nums[num] = 1

        # if the current number is not zero and it's inverse is already in the dict,
        # add the current number's absolute value to the result list
        if num != 0 and -num in nums:
            result.append(abs(num))

    # return the resulting list of numbers
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
