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


print (fibd(94, 16))