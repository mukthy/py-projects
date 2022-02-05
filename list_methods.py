

basket = [1, 2, 3, 4, 5]

# adding a new item to a list

basket.append(100)
add_basket = basket

print(add_basket)

# inster an item to a list
basket.insert(3, 25)
insert_basket = basket

print(insert_basket)

# extend your list by adding more items.
basket.extend([101, 102])
extend_basket = basket

print(extend_basket)

# removing items from the list using pop() and remove()

basket.pop()  # this will remove the last item from lthe list just like "Last in first out"
pop_basket = basket

print(pop_basket)

# this will remove the item whose index value is mentioned in pop() from the list.
basket.pop(1)
pop_basket = basket

print(pop_basket)

# this will return the poped out item from the list, for eg: it will return 100.
new_pop_basket = basket.pop(5)
print(new_pop_basket)

# this will remove the item whose value is mentioned in remove() from the list.
basket.remove(25)
remove_basket = basket

print(remove_basket)

#clear_list = basket.clear()
# print(clear_list)
# print(basket)

basket_list = ['a', 'b', 'c', 'd', 'e', 'a']
# this prints the index value of an item which is passed in the index(value) which is part of the basket_list.
index = basket_list.index('c')

print(index)

# this 'in' will help in checking if an item is in the list or not by giving True or False as an output
print('b' in basket_list)

print('f' in 'mukthy')

# this will return a value on how many times an item is present in a list.
print(basket_list.count('a'))

basket_sort = ['a', 'b', 'd', 'e', 'c']

basket_sort.sort()  # this will modify the list by sorting it.
print(basket_sort)


basket_sorted = ['a', 'b', 'd', 'e', 'c']

# sorted is a function which does not modify a list it actually creats a copy of the list and modifies by sorting the copied list.
print(sorted(basket_sort))
print(basket_sorted)

# for copying a sorted List we can also use a .copy() method.

copy_basket = ['a', 'b', 'd', 'e', 'c']
copied = copy_basket.copy()
print(f'this is copied {copied}')

reverse_basket = ['c', 'a', 'b', 'b', 'c', 'd', 'e', 'x']
# reverse_basket.sort()
# this reverse method will only reverse the items list and print it. It will not sort and reverse.
reverse_basket.reverse()
print(reverse_basket)


reverse_basket = ['c', 'a', 'b', 'b', 'c', 'd', 'e', 'x']

reverse_basket.sort()
# This method will modify the existing list by reversing it.
reverse_basket.reverse()
# We can also reverse a list using this [::-1] but this will create a new version of the existing list like a copy instead of modifying the exisitng list.
print(reverse_basket[::-1])
print(reverse_basket)


# To quicly generate a list we can use a range function wraped with a list function.
print(list(range(0, 10)))

# this ' '.join() is used to join the items in the list just like a string or a sentence.
new_sentence = ' '.join(['my', 'name', 'is', 'mukthy'])
print(new_sentence)

# in list unpacking we can unpack items of the list like a,b,c and also to get other items in the list we can use *others to get it.
a, b, c, *others, d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(others)
print(d)
