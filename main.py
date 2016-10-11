import random

rand_list = []

while (len(rand_list) != 15):
 rand_list.append(random.randrange(0,100))
print(rand_list)

b = 0
a = 0
end = len(rand_list)
while end != 2:
    print(end)
    while a + 1 != end:
        if rand_list[a] > rand_list[a + 1]:
            b = rand_list[a]
            rand_list[a] = rand_list[a + 1]
            rand_list[a + 1] = b
            a += 1
        else:
            a += 1
    a = 0
    b = 0
    end -= 1
    print(rand_list)