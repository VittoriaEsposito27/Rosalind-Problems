def tree(n, edges):
    return n - len(edges) - 1

if __name__ == '__main__':
    dataset = open("rosalind_tree.txt").readlines()
    n = int(dataset[0])
    edges = []
    for i in range(1, len(dataset)):
        edges.append(map(int, dataset[i].split()))
    print tree(n, edges)