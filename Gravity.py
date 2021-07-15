boxes = list(map(int, input().split()))
# boxes = [3, 4, 2, 0, 0, 6, 0, 7, 0]
pile = [0] * max(boxes)
boxes.reverse()
result = 0

for i in range(len(boxes)):
    box = boxes[i]
    for j in range(box):
        if  i > pile[j]:
            result = max(result, i - pile[j])
        pile[j] += 1    

print(result)
