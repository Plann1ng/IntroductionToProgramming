boxes = 0
candles = 0
total = 0
for age in range(1, 101):
    if candles < age:
        if (age-candles) < 24:
            box = 1
        else:
            if (age-candles) % 24 == 0:
                box = int((age-candles)/24)
            else:
                box = int((age-candles)/24 + 1)
        candles = candles + (box*24) - age
    else:
        box = 0
        candles = candles-age
        print(candles)
    if box != 0:
        print("Before birthday ", age, ", buy ", box, " box(es)")
    total = total + box
print("\nTotal number of boxes: ", total, ", Remaining candles: ", candles)
