# while loop will keep running until the condition is fales or satiesfied.
# this below case results in an infinite loop.
from urllib import response


i = 0
while i < 50:
    print(i)
    # break is usually used to break the while loop from entering an infinite loop.
    break

while i < 50:
    print(i)
    i += 1
    break
else:
    print("Done with printing all numbers")

while True:
    response = input("Say Something: ")
    if response == "bye":
        break
 