import sys
n = int(input())
d = {}

for _ in range(n):
  val = input().split()
  d[val[0]] = int(val[1])

time = list(d.values())
s = 0
burst_time=[]
burst_time.append(0)
for j in time:
    s = s + j
    burst_time.append(s)

# dictionary wil list only the key values
for (k,m) in zip(list(d), burst_time):
    sys.stdout.write(str(m)+" "+str(k)+" ")
  
sys.stdout.write(str(burst_time[-1])+" ")
print(f'Average Time : {sum(burst_time[:-1])/n}')