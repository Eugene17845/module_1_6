my_dict={'Женя':2002,'Вика':2001,'Ника':1999}
print('Список:',my_dict)
print('Сущ. кл.:',my_dict['Женя'])
print('Несущ. кл.:',my_dict.get('Геля'))
(my_dict .update({'Витя':2005,'Коля':2002,'Вася':1986}))
f=my_dict.pop('Ника')
print('Уд. кл.:',f)
print('Изм. список:',my_dict)

my_set={1, 17.2,'Игла'}
print('Список:',my_set)
my_set.update(['D',('Игорь', 6, 6.6)])
my_set.discard(1)
print('Изм. список:', my_set)
