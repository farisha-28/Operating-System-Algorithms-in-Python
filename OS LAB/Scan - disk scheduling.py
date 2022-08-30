import sys
r = list(map(int, input("Enter the requests: ").split()))
head = int(input("Head: "))
largest = int(input("Largest: "))
small = int(input("Smallest: "))
r.append(head)
r.append(small)

r.sort()
small_ind = r.index(small)
head_ind = r.index(head)

# left - 0 to head
left_half = r[small_ind:head_ind+1]
# now head to 0 [ 53 to 0]
left_half.sort(reverse=True)
# 65 to last
right_half = r[head_ind+1:len(r)]
summ = 0
concat = str()

# left half in descending manner 53,37,14,0
for k in range(0,len(left_half)-1):
    sys.stdout.write(str(left_half[k]) + " ")
    temp = abs(left_half[k]-left_half[k+1])
    summ = summ+temp
    concat = concat + "+" + "({} - {})".format(left_half[k],left_half[k+1])

sys.stdout.write(str(small) + " ")
head = small

# right half -- 65,67,98, 122 ......
for j in right_half:
    temp = abs(j-head)
    sys.stdout.write(str(j) + " ")
    summ = summ + temp
    concat = concat + "+" + "({} - {})".format(j, head)
    head = j

print("Summation is : ",summ)
print(concat[1:])