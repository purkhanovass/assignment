def replace_value(values, index, new_value):
    values[index] = new_value
def find_first(values,target):
    for i in range(len(values)):
        if values[i] == target:
            return i
        return -1
def summarize(values):
        return (min(values), max(values), sum(values))
day = int(input('Enter the number of days:'))
original = []
for i in range(day):
    exercise_time = int(input("Enter the exercise time in minutes: "))
    original.append(exercise_time)
updated = original[:]
index = int(input("Enter the index: "))
new_exercise_time = int(input("Enter the new practice time:"))
replace_value(updated, index, new_exercise_time)
target = int(input("Enter the exercise time to search for "))
target_index = find_first(updated, target)
target_count = updated.count(target)
minimum, maximum, total = summarize(updated)  # tuple unpacking 
sorted_updated = sorted(updated)

print(f'Original: {original}')
print(f'Updated: {updated}')
print(f'Sorted: {sorted}')
print(f'The shortest exercise time: {minimum} minutes')
print(f'The longest exercise time: {maximum} minutes')
print(f'The total exercise time: {total} minutes')

if target_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {target_index}")

print(f"Matching values: {target_count}")
