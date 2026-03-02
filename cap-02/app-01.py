y = 1
y_list = [y]
t = 0
tf = 1
n = 10
h = tf/n
t_list = [t]

for i in range(0, n):
    t = t+h
    y = y+h*y
    t_list.append(t)
    y_list.append(y)

print(t_list)
print(y_list)
