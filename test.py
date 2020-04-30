course_id = 1
context = {}
while course_id < 5:
    context["users" + str(course_id)] = course_id
    course_id += 1
print(context)
