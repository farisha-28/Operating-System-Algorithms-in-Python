import sys
n = int(input("No of process: "))
d = {}

for _ in range(n):
  val = input().split()
  d[val[0]] = [int(val[1]), int(val[2])]

# sort according to the priority queue
dic_srt = sorted(d.items(), key=lambda item:item[1][1])

time = []
s = 0
time.append(s)
for i in dic_srt:
  # summ up burst time from sorted dict and append to time
  s = s + i[1][0]
  time.append(s)
print(time)

# k[0] means process name
for (k,m) in zip(dic_srt,time):
  sys.stdout.write(str(m)+" "+str(k[0])+" ")
sys.stdout.write(str(time[-1])+" ")

print(f'Average waiting time : {sum(time[:-1])/n}')