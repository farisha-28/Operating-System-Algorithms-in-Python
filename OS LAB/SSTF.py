import sys
n = int(input())
queue = list(map(int,input().strip().split()))
head = int(input())
queue.append(head)
queue.sort()
print("Sorted queue : ",queue)
head_index = queue.index(head)
print("Path : ")
sys.stdout.write(str(head)+" ")

left = queue[head_index-1]
left_diff = abs(head - left)
left_ind = queue.index(left)

right = queue[head_index+1]
right_diff = abs(head - right)
right_ind = queue.index(right)
concatn = str()
summ = 0

for i in range(0, len(queue)-1):

    if right_diff < left_diff:
        sys.stdout.write(str(right) + " ")
        prev_head = head
        head = right
        summ = summ+abs(prev_head-head)
        if head > prev_head:
            concatn = concatn + "+" + "({} - {})".format(head, prev_head)
        else:
            concatn = concatn + "+" + "({} - {})".format(prev_head, head)
        head_index = queue.index(head)
        left_diff = abs(head - left)
        right_diff = abs(head - queue[head_index + 1])
        right = queue[head_index + 1]

    else:
        sys.stdout.write(str(left) + " ")
        prev_head = head
        head = left
        summ = summ + abs(prev_head - head)
        if head>prev_head:
            concatn = concatn + "+" + "({} - {})".format(head, prev_head)
        else:
            concatn = concatn + "+" + "({} - {})".format(prev_head, head)
        head_index = queue.index(head)
        left_diff = abs(head - queue[head_index - 1])
        right_diff = abs(head - right)
        left = queue[head_index - 1]

print("Summation of track seek time : ",summ)
print("Difference of Seek time between each track : ",concatn[1:])


