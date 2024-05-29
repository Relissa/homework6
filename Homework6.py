#Словари
my_dict = {'Алексей': 1991, 'Юлия': 1974, 'Семён': 2004, 'Ирина': 1993}
print('Dict: ' + str(my_dict))
print('Existing value: ' + str(my_dict['Юлия']))
print('Not existing value: ' + str(my_dict.get('Мария')))
my_dict.update({'Светлана': 1988, 'Диана': 1999})
x = my_dict.pop('Семён')
print('Deleted value: ' + str(x))
print('Modified dictionary: ' + str(my_dict))
# Множества
my_set = {1, 2, 3,'work', 3, 2, 1, 4, False, 5}
print('Set: ' + str(my_set))
my_set.update({'problem', 7})
my_set.discard(3)
print('Modified set: ' + str(my_set))
