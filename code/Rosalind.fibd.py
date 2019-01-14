def fibd(i, j):
    generations = [1, 1]
    count = 2
    while (count < i):
        if (count < j):
            generations.append(generations[-2] + generations[-1])
        elif (count == j or count == j+1):
            generations.append((generations[-2] + generations[-1]) - 1)
        else:
            generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)]))
        count += 1
    return (generations[-1])


if __name__ == "__main__":
    f = open('rosalind_fibd.txt').read()
    x, y = map(int, f.split())
    print(fibd(x,y))
