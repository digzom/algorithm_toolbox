n = int(input())
m = input()

array = m.split()

int_array = []

for element in array:
    int_array.append(int(element))


int_array.sort()

biggest_n = int_array.pop()
second_biggest_n = int_array.pop()

maximum_pairwise_product = second_biggest_n * biggest_n

print(maximum_pairwise_product)
