import glob
import numpy as np
import matplotlib.pyplot as plt
my_list = []
for filename in glob.glob('data/*.txt'):
    fp = open(filename)
    for i, line in enumerate(fp):
        if i == 6:
            my_list.append((str(filename)[5:-4], float(str(line)[31:-1])))
print my_list
people = []
grade = []
for i in my_list:
    people.append(i[0])
    grade.append(i[1])
print tuple(people)
y_pos = np.arange(len(people))

performance = tuple(grade)

error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()
