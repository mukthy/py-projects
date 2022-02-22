class SuperList(list):  # since this class is alway a subclass of pre-defined classes in python we can inherit the List class in our SuperList. So that we can use methods such as .append()
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(1)
print(super_list1[0])
