#Packed Arguments
def subjects(*marks):
    total = 0
    for i in marks:
        total += i
    print(total)

subjects(10,10,10)

#keyword Argument
def g_form(**keyword):
    if 'name' not in keyword:
        print("Error")
    else:
        print("Hello" , keyword['name'])

    if 'age' not in keyword:
        print("Error")
    else:
        print("You are", keyword['age'] , "years old")

    if 'city' not in keyword:
        print("Error")
    else:
        print("You're from" , keyword['city'])

g_form(name = "Hansaka" , age = 18 , city = "Maradankadawala")
g_form(age = 19 , city="kekirawa")

#Return
def grade(marks):

    if marks < 0 or marks > 100:
        print ("Invalid")
    elif marks < 35:
        get_grade = "W"
    elif marks < 55:
        get_grade = "C"
    elif marks < 65:
        get_grade =  "B"
    else:
        get_grade = "A"

    print("Hansaka Vidushan")
    return get_grade

get_grade = grade(55)
print(get_grade)


