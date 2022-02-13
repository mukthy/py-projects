def highest_even(li):
    new_li = []
    # to check the even numbers from the given list of numbers and append it to a new list.
    for item in li:
        if item % 2 == 0:
            new_li.append(item)
    print(new_li)

    # to check the highest from the new list new_li which only contains the even numbers.
    highest_even = 0
    for item in new_li:

        if item > highest_even:
            highest_even = item

    return highest_even


print(highest_even([20, 2, 3, 8, 30, 35, 10]))
