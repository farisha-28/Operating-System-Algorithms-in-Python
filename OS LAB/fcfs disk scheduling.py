import sys
n = int(input())
queue = list(map(int,input().strip().split()))
head = int(input())
first_head = head
summ = 0
concat = str()
# k = []
sys.stdout.write("Requested queue : "+str(head)+" ")

for i in range(n):
  sys.stdout.write(str(queue[i])+ " ")
  temp = abs(queue[i]-head)
  summ = summ+temp

  if queue[i]>head:
    # k.append("({} - {})+".format(l[i],head))
    concat = concat + "+" + "({} - {})".format(queue[i],head)
  else:
    # k.append("({} - {})+".format(head,l[i]))
    concat = concat + "+" + "({} - {})".format(head, queue[i])
  head = queue[i]

print("Summation is : ",summ)
# print(",".join(k))
print(concat[1:])


