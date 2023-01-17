
import random
n = int(input("values to be generated: "))
print("Generated values:", end=" ")
total = 0

max_value = 0
rndm_list = []
for i in range(n):
    r = random.randint(1, 100)
    total += r/n
    rndm_list += [r]
    print(r, end=" ")
print("\nAvereage, min, and max are", round(total, 1), ",", end="")
print(min(rndm_list), "and", max(rndm_list), sep=" ")