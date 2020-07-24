import random

length_of_list = random.randint(1, 30)
complex_num_list = []

for i in range(0, length_of_list):
    print(str(random.randint(0, 500)) + "+" + str(random.randint(0, 500)) + "i, ", end="")
print("\n")
