# Accessing tuple value
t1 = (10, 20, 30, 40, 50, 60, 70, 80)
print(t1)

# Accessing tuple negative value
t2 = (10, 20, 30, 40, 50, 60, 70, 80)
print(t2[-2])

# Accessing tuple value in range
t3 = (10, 20, 30, 40, 50, 60, 70, 80)
print(t3[0:4])

# change tuple value
t4 = (10, 20, 30, 40, 50, 60, 70, 80)
i = list(t4)
i[3]=100
print(i)
j = tuple(i)
print(j)

# FETCH TUPLE VALUE WITH FOR LOOP
t4 = (10, 20, 30, 40, 50, 60, 70, 80)
for i in t4:
    print(i)

# tuple length
t4 = (10, 20, 30, 40, 50, 60, 70, 80)
print(len(t4))

# Delete tuple
t4 = (10, 20, 30, 40, 50, 60, 70, 80)
print(t4)
del t4


# merge two tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
print(tuple1 + tuple2)
