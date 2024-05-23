import math

people_count = int(input())
capacity = int(input())

courses_count = math.ceil(people_count / capacity)

# if people_count % capacity == 0:
#     courses = int(people_count / capacity)
# else:
#     courses = int(people_count/capacity) + 1

print(courses_count)
#print(courses)

