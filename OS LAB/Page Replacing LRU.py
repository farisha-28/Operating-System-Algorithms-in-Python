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
            if p in pages[0:i]:
                temp = pages[0:i]
                temp.reverse()
                ind_next = len(temp) - temp.index(p) - 1
                indices.update({p: ind_next})

        keys = list(indices.keys())
        vals = list(indices.values())
        minimum = min(vals)
        pos = vals.index(minimum)
        m = memory.index(keys[pos])
        memory[m] = pages[i]
        s = np.array(memory)
        print(str(s)[1:-1])
        fault = fault+1
        del indices[keys[pos]]

    elif pages[i] in memory:
        l = len(memory)
        hit = hit+1
        print('-'*l, sep=' ')

# print("Total Hits: ",hit)
# print("Total Faults: ",fault)
