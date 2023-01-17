import random

def fallen(size, steps, sailors):
    fallen = 0

    for i in range(sailors):
        hor = 0
        ver = 0
        for steps in range(-size,size):
            for i in range(steps):
                direction = random.randint(1, 4)
                if direction == 1:
                    ver += 1
                elif direction == 2:
                    hor += 1
                elif direction == 3:
                    ver -= 1
                elif direction == 4:
                    hor -= 1
        if hor >= size or hor <= -size  or ver >= size or ver <= -size :
            fallen += 1

    return fallen

size = int(input("Please enter size: "))
steps = int(input("Please provide number of steps: "))
sailors = int(input("Please enter number of sailors: "))

fallen = fallen(size, steps, sailors)
perc = round(fallen / sailors * 100, 2)

print(f"\nOut of {sailors} drunk sailors, {fallen} ({perc}%)", end=" ")
print("fell into the water.")
