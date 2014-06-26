from time import time
list_insert = []
list_append = []
list_extend = []

def check_insert_back():
    list_of_times_insert = []
    ranges = [1000,10000,100000,200000]

    for i in ranges:
        list_insert = []
        now =time()
        for j in xrange(i):
            list_insert.insert(len(list_insert),j)
        then = time()
        list_of_times_insert.append([i,then-now])

    with open("insert_method_back_list.txt","w") as f:
        for i in list_of_times_insert:
            f.write(str(i[0])+","+str(i[1])+"\n")

def check_insert_front():
    list_of_times_insert = []
    ranges = [1000,10000,100000,200000]

    for i in ranges:
        list_insert = []
        now =time()
        for j in xrange(i):
            list_insert.insert(0,j)
        then = time()
        list_of_times_insert.append([i,then-now])

    with open("insert_method_front_list.txt","w") as f:
        for i in list_of_times_insert:
            f.write(str(i[0])+","+str(i[1])+"\n")


def check_extend():
    list_of_times_extend = []
    ranges = [1000,10000,100000,200000]

    for i in ranges:
        list_extend = []
        now =time()
        for j in xrange(i):
            list_extend.extend([j])
        then = time()
        list_of_times_extend.append([i,then-now])

    with open("extend_method_list.txt","w") as f:
        for i in list_of_times_extend:
            f.write(str(i[0])+","+str(i[1])+"\n")

def check_append():
    list_of_times_append = []
    ranges = [1000,10000,100000,200000]
    
    for i in ranges:
        list_append = []
        now =time()
        for j in xrange(i):
            list_append.append(j)
        then = time()
        list_of_times_append.append([i,then-now])

    with open("append_method_list.txt","w") as f:
        for i in list_of_times_append:
            f.write(str(i[0])+","+str(i[1])+"\n")

def check_remove():
    list_of_times_remove = []
    ranges = [1000,10000,100000,200000]

    for i in ranges:
        listing = range(i)
        now =time()
        for j in xrange(i):
            listing.remove(j)
        then = time()
        list_of_times_remove.append([i,then-now])

    with open("remove_method_list.txt","w") as f:
        for i in list_of_times_remove:
            f.write(str(i[0])+","+str(i[1])+"\n")

def check_pop():   
    list_of_times_pop = []
    ranges = [1000,10000,100000,200000]

    for i in ranges:
        listing = range(i)
        now =time()
        for j in xrange(i):
            listing.pop()
        then = time()
        list_of_times_pop.append([i,then-now])

    with open("pop_method_list.txt","w") as f:
        for i in list_of_times_pop:
            f.write(str(i[0])+","+str(i[1])+"\n")



check_insert_back()
#check_insert_front()
check_extend()
check_append()
#check_remove()
check_pop()
