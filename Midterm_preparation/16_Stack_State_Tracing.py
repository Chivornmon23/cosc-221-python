stack = [] # 60
result = [] #15, 30, 45, 60
items = [15, 30, 45, 60]

for x in items:
    if x % 20 == 0:
        stack.append(x) #60
    else:
        result.append(x)
while stack:
    result.append(stack.pop())

print(result) #[15, 30, 45, 60]