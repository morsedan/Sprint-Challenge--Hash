def intersection(arrays):

    """
    YOUR CODE HERE
    """
    arrays = sorted(arrays, key=lambda x: len(x))
    num_dict = {}
    result = []
    for element in arrays[0]:
        num_dict[element] = 1
    for array in arrays[1:]:
        for element in array:
            if element in num_dict:
                num_dict[element] += 1
    result = [num for num in num_dict if num_dict[num] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])
    # arrays.append([1,2,3])
    # arrays.append([1])
    # arrays.append([1,2])
    print(intersection(arrays))
