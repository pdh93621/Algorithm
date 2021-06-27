array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
visited = [0] * len(array)

for i in array:
    visited[i] += 1

new_array = []
for v in range(len(visited)):
    for i in range(visited[v]):
        new_array.append(v)

print(new_array)