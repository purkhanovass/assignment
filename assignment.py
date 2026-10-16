bag = int(input("Enter the number of tiles: "))
s = 0
below = 0
inrange = 0
above = 0


def classify(b):
    if b < 1998:
        return "Below range"
    elif 1998 <= b <= 2002:
        return "In range"
    else:
        return "Above range"


for i in range(bag):
    weight = int(input("Enter the tile width: "))
    s += weight
    cat = classify(weight)
    print(cat)
    if cat == "Below range":
        below += 1
    elif cat == "In range":
        inrange += 1
    else:
        above += 1


def calculate_average(total, count):
    return total / count


avg = calculate_average(s, bag)
print(f"Total width: {s} g")
print(f"Average width: {avg} g")
print(f"Below range: {below}")
print(f"In range: {inrange}")
print(f"Above range: {above}")