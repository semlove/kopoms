item = [1, 3, 390, 77, 88, 141]
max = item[0]
min = item[0]
for i in item:
  if i < min:
    min = i
  if i > max:
    max = i
print(max)
print(min)