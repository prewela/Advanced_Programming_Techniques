class FenwickTreeMax:
    def __init__(self, size):
        self.size = size
        self.tree = [float('-inf')] * (self.size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)
            index += index & -index

    def query(self, index):
        # Maximum over the interval [1:index]
        result = float('-inf')
        while index > 0:
            result = max(result, self.tree[index])
            index = index & (index - 1)
        return result


def filter_scores(scores, n = None):
    # Sort scores by column 0
    scores = sorted(scores, key = lambda x: (x[0], x[1], -x[2]))

    # Map scores in 1st column
    unique_values = sorted(set(x[1] for x in scores))
    value_map = {val: i + 1 for i, val in enumerate(unique_values)}
    mapped_scores = [[x[0], value_map[x[1]], x[2]] for x in scores]

    if n is None:
        n = len(scores)

    # Initialize Fenwick Tree
    tree = FenwickTreeMax(n)
    for i in range(1, n+1):
        tree.update(i, 0)
    
    # Find unnecessary scores
    to_remove = [1 for i in range(n)]    #remove score if 0, keep score if 1
    for i, x in enumerate(mapped_scores):
        if tree.query(x[1]) > x[2]:  
            to_remove[i] = 0    
            continue
        tree.update(x[1], x[2])

    # Filter scores
    scores_filtered = [i for i, j in zip(scores, to_remove) if j == 1]
    return scores_filtered


def read_data(file):
    with open(file, "r") as f:
        lines = f.readlines()

    n = int(lines[0])
    scores = [None for i in range(n)]
    for i in range(n):
        scores[i] = list(map(int, lines[i+1].split()))
    return scores, n


if __name__ == "__main__":

    scores, n = read_data("input.txt")
    filtered_scores = filter_scores(scores, n)
    k = len(filtered_scores)

    print("Filtered scores:")
    for i in range(k):
        print(filtered_scores[i])
    print("Number of scores: ", k)
    