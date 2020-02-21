class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """

    def logSort(self, logs):
        nums = []
        letters = []
        for log in logs:
            temp = log.split(" ")
            if temp[1].isdigit():  # if the content is digit, put in there input order
                nums.append(log)
            else:
                letters.append((" ".join(temp[1:]), temp[0]))  # creat a tuple for that, and sort all letter log
                print((" ".join(temp[1:]), temp[0]))
        letters.sort()

        let = []
        for letter in letters:  # Because we use reverse sequence to store, we should append[1], then[0]
            let.append(letter[1] + " " + letter[0])

        return let + nums
        # return [letter[1] + " " + letter[0] for letter in letters] + nums