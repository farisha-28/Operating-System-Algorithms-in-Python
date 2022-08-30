import sys

quantam = int(input("Quantam Value: "))
n = int(input("Total Processes: "))
d = {}
for _ in range(n):
    val = input().split()
    d[val[0]] = int(val[1])

q, mod = divmod(max(d.values()), quantam)
s = 0
time = []
key_list = []
turn_around = []
d_val = list(d.values())
time.append(0)
# in dictionary all process and burst time is stored..through iteration burst time will be updated
for i in range(q + mod):
    for j in d:
        # j is the process ; p is the process left burst time
        p = d.get(j)
        if p != -1:
            # when still left bust time is greater or equal to quantam
            if p >= quantam:
                s = s + quantam
                time.append(s)
                key_list.append(j)
                rem = p - quantam
                d.update({j: rem})
            # last time taken by each process will be turnaround time
            elif p < quantam:
                s = s + p
                time.append(s)
                turn_around.append(s)
                key_list.append(j)
                # when time becomes less than quantam val, it won't work again., so set its value in dict as -1
                d.update({j: -1})
# for printing zip two lists....iterate over both
for (k, m) in zip(time, key_list):
    sys.stdout.write(str(k) + " " + str(m) + " ")
sys.stdout.write(str(time[-1]) + " ")

summ = 0
for (k, m) in zip(turn_around, d_val):
    summ = summ + (k - m)

print(f'Average Turn Around Time: {sum(turn_around) / len(turn_around)}')
print(f'Average Waiting Time: {summ / len(turn_around)}')