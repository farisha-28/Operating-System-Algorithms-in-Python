import sys
r = list(map(int, input("Enter the requests: ").split()))
head = int(input("Head: "))
largest = int(input("Largest: "))
small = int(input("Smallest: "))
r.append(head)
r.sort()
head_ind = r.index(head)

left_half = r[:head_ind]
right_half = r[head_ind:len(r)]
summ = 0
concat = str()

for i in range(0,len(right_half)-1):
    sys.stdout.write(str(right_half[i]) + " ")
    head = right_half[i+1]
    temp = abs(head - right_half[i])
    summ = summ + temp
    concat = concat + "+" + "({} - {})".format(head, right_half[i])
sys.stdout.write(str(head) + " ")

for j in left_half:
    sys.stdout.write(str(j) + " ")
    temp = abs(head-j)
    summ = summ + temp
    if head>j:
        concat = concat + "+" + "({} - {})".format(head,j)
    else:
        concat = concat + "+" + "({} - {})".format(j, head)
    head = j

print("Summation is : ",summ)
print(concat[1:])


