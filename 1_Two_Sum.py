class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        d = {}  # create a hashmap to store the value
        res = []  # initialize a result list
        for i in range(len(numbers)):  # traverse the numbers
            comp = target - numbers[i]  # define comp = target - index

            if comp in d:  # if comp in dict, return its value
                return [d[comp], i]  # which is index of that comp

            else:
                d[numbers[i]] = i  # if not in the dict, add the value as key, index as value