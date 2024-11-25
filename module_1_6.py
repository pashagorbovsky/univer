#1s task
my_dict = {'one': [2,3,4,1],'two': [1,6,8,4],'three': [5,3,7,4],'four': [9,1,1,3]}
print(my_dict['one'])
print(my_dict.get('five'))
my_dict.update ({'five': [3,2,6,7],'six': [5,6,3,3]})
a = my_dict.pop('three')
print(a)
print(my_dict)

#2nd task

my_set = {23,'one',True,'two',True,False,'one',45,23.5,23,'one','three',23.5}
print(my_set)
my_set.add(666)
my_set.add('five')
my_set.remove(23)
print(my_set)