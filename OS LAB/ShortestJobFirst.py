import sys
n = int(input())
d = {}
for _ in range(n):
  val = input().split()
  d[val[0]] = int(val[1])

dic_time = sorted(d.items(), key=lambda kv:(kv[1], kv[0]))
s = 0
burst_time=[]
burst_time.append(0)

for j in dic_time:
    s = s + j[1]
    burst_time.append(s)
  
for (k,m) in zip(dic_time, burst_time):
    sys.stdout.write(str(m)+" "+str(k[0])+" ")
  
sys.stdout.write(str(burst_time[-1])+" ")
print(f'Average waiting time : {sum(burst_time[:-1])/n}')