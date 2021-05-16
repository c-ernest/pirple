Loop = []

counter = 1

while counter <= 100:

    count = 0
    
    Loop.append(counter)
    counter = counter + 1

    if counter%3 == 0:
        Loop.append("Fizz")
    if counter%5 == 0:
        Loop.append("Buzz")
    if (counter%3 == 0) and (counter%5 == 0):
        Loop.append("FizzBuzz")

print(Loop)


