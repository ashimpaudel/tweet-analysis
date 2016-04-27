import glob
import operator
import numpy as np
import matplotlib.pyplot as plt
my_list = []
for filename in glob.glob('data/*.txt'):
    fp = open(filename)
    for i, line in enumerate(fp):
        if i == 26:
            my_list.append((str(filename)[5:-4], float(str(line)[29:-1])))
#print my_list
people = []
grade = []
my_dict = {}
for i in my_list:
    keys = i[0]
    values=  i[1]
    my_dict[keys] = values
    people.append(i[0])
    grade.append(i[1])
#print tuple(people)
#print my_dict
y_pos = np.arange(len(people))

performance = tuple(grade)

error = np.random.rand(len(people))
sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))
print type(sorted_dict)
new_grade = []
new_people = []
for i in sorted_dict:
    new_grade.append(i[1])
    new_people.append(i[0])
    

print 'people ise', people
print 'performance is ', performance
print 'y_pos', y_pos
performance = tuple(new_grade)

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, new_people)
plt.xlabel('Coleman-Liau INDEX')
plt.title('Coleman-Liau INDEX of:')

plt.show()



