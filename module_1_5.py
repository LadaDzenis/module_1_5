immutable_var = (111, True, "Lada", 10.10)
print("Immutable tuple: " + str(immutable_var))
# immutable_var [0] = 222
# print(immutable_var)
# изменение элемента кортежа невозможно, так как это неизменяемый объект
mutable_list = [111, True, "Lada", 10.10]
mutable_list [0] = 222
mutable_list [1] = False
mutable_list [2] = "Dzenis"
print("Mutable list: " + str(mutable_list))