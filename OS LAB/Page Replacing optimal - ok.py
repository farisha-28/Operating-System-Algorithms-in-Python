import numpy as np
n = int(input("Total pages: "))
pages = list(map(int,input("Requested String: ").strip().split()))
capacity = int(input("Main Memory Capacity: "))
memory = []
indices = {}
hit = 0
fault = 0
m = 0
maximum = 0
k = 0

for i in range(n):
    # 7--len=0,0---len=1,1---len=2, 2---len=3
    # for only first 3 elements (7,0,1)
    if pages[i] not in memory and len(memory)<capacity:
        memory.append(pages[i])
        m = np.array(memory)
        print(str(m)[1:-1], "-" * (capacity - len(memory)))
        fault = fault + 1

        # for 4th element till the last element
    elif pages[i] not in memory and len(memory) == capacity:

        for p in memory:
            if p in pages[i+1:n]:
                ind_next = pages[i + 1:n].index(p)
                indices.update({p: ind_next})

            else:
                ind_next = n+1
                indices.update({p: ind_next})

        # those values are now in indices dict who were in the memory
        keys = list(indices.keys())
        vals = list(indices.values())
        maximum = max(vals)

        # to get the value of maximum index
        pos = vals.index(maximum)
        m = memory.index(keys[pos])

        # replace that value with the new value
        memory[m] = pages[i]

        # print the new memory
        s = np.array(memory)
        print(str(s)[1:-1])
        fault = fault+1
        # delete that maximum value from the indices
        del indices[keys[pos]]

    elif pages[i] in memory:
        l = len(memory)
        hit = hit+1
        print('-'*l, sep=' ')

# print("Total Hits: ",hit)
# print("Total Faults: ",fault)
