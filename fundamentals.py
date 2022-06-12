# coding=utf-8
# ACTDEV Fundamentals is a mental arithmetic workout

questions = 10
x = 100
y = 10


for num in range(1,questions):
    a = random(x)
    b = random(y)
    c = 1 # random(4)
    answer = 0
    solution = 0

    print("Question " + num)
    switch(c):
        case 1: 
            print(a " + " b)
            answer = input("Enter answer: ")
            solution = x + y
            break
        case 2: 
            solution = x - y
            break
        case 3:
            solution = x * y
            break
        case 4:
            solution = x / y
            break

    if (solution == answer):
        print("correct")
    else:
        print("incorrect: " + solution)