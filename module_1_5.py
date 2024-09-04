# immutable_var = (1, 2, 3, True , "String")
# tuple_ = immutable_var
# print(immutable_var)
# immutable_var[0] = 4
# print(immutable_var)
# кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3, True, "String"]
tuple_2 = mutable_list
print(mutable_list)
mutable_list[0] = 8
mutable_list[3] = False
mutable_list[2] = 7 + 7
print(mutable_list)