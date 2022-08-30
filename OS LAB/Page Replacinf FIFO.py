import numpy as np
n = int(input("Total pages: "))
pages = list(map(int,input("Requested String: ").strip().split()))
capacity = int(input("Main Memory Capacity: "))
memory = []
hit = 0
fault = 0
flag = 1


for i in range(n):
    # 7--len=0,0---len=1,1---len=2, 2---len=3
    if pages[i] in memory:
        l = len(memory)
        hit = hit+1
        print('-'*l, sep=' ')

    elif pages[i] not in memory and len(memory)<capacity:
        memory.append(pages[i])
        m = np.array(memory)
        print(str(m)[1:-1], "-"*(capacity-len(memory)))
        fault = fault+1
        flag = 0

    elif pages[i] not in memory and len(memory) == capacity:
        memory[flag] = pages[i]
        s = np.array(memory)
        print(str(s)[1:-1])
        fault = fault+1
        flag += 1

        # when we have replaced all the 3 elements in memory, then again start from flag 0, from first element
        if flag == capacity:
            flag = 0

# print("Total Hits : ",hit)
print("Total Faults : ",fault)

# removing brackets and comma from list
# lst = [11,33,22,99]
# s = str(lst)
# s = s.replace(',', ' ')
# print(s[1:-1])
#
