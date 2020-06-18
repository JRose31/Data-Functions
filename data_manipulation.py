import statistics
import numpy as np

#sort multiple list at once, utilizing the first argument as the sort rule
def sort_list(*args):

    #check to ensure length of all lists are the same making the first list the rule
    accept_length = len(args[0])
    len_ok = None

    for arg in args:
        if len(arg) != accept_length:
            len_ok = False
        else:
            len_ok = True

    if len_ok == True:
        #sort both list by first parameter
        args = sorted(zip(*args))

        #retrieves number of arguments passed
        length = len(args[0])

        #initializes new list for results to be returned as a tuple for multi-variable assignment
        results = []

        #counter starts index, creating each list
        counter = 0

        while counter < (length):
            #initialize new list to contain original list argument but sorted
            add_list = []

            for i in args:
                add_list.append(i[counter])

            #add each list to entire results list
            results.append(add_list)
            counter += 1

        return(tuple(results))

    else:
        print("***LISTS ARE NOT EQUAL***")


x = [1, 3, 5, 2, 4, 3 ]
z = ["one", "three", "five", "two", "four", "three"]
y = ["uno", "tres", "cinco", "dos", "quatro", "tres"]
n, i, o = sort_list(x, z, y)

print(n) #returns [1, 2, 3, 3, 4, 5]
print(i) #returns ["one", "two", "three", "three", "four", "five"]
print(o) #returns ["uno", "dos", "tres", "tres", "quatro", "cinco"]



'''
converts missing values in a list to the mean of the list
***currently only accepts one list argument***
'''
def avgna(n, *args):

    #initialize list to hold null values
    null_vals = []

    #list without null values (used to get mean of set)
    num_vals = []

    #counter for indexing
    counter = 0

    for i in n:

        '''check if instance is a number, if so, add to valid set. If instance
        is not a number, get index of instance and the current value'''
        try:
            int(i)
            num_vals.append(i)
        except:
            null_vals.append([counter, i])

        counter+=1

    '''get mean of good data
    if argument is passed, return specified number of decimal points'''
    if len(args) < 1:
        avg = round(statistics.mean(num_vals), 2)
    else:
        avg = round(statistics.mean(num_vals), args[0])

    #add new values in place of NaN
    for i in null_vals:
        num_vals.insert(i[0], avg)

    return(num_vals)

x = [1, 3, 2, 6, "NaN", 5, 8, " ", "!", 7]
n = avgna(x)
print(n) #returns [1, 3, 2, 6, 4.57, 5, 8, 4.57, 4.57, 7]

#passing an additional numerical argument specifies number of decimal places to return
n = avgna(x, 3)
print(n) #returns [1, 3, 2, 6, 4.571, 5, 8, 4.571, 4.571, 7]


#removes rows with missing values
def delna(*args):

    #initialize list to hold null values
    null_vals = []

    #length_data = len(args[0])

    for arg in args:

        counter = 0

        for i in arg:
            try:
                int(i)
                counter += 1
            except:
                null_vals.append([counter, i])
                counter += 1

    #get unique indices of null values
    index = []
    for i in null_vals:
        if i[0] not in index:
            index.append(i[0])

    #initialize list of results
    results = []

    #delete same indices in all list, add to result list
    for arg in args:
        n = np.delete(arg, index).tolist()
        results.append(n)

    return(tuple(results))

x = [1, 3, "fvd", 546, "ffd", 6, 3]
y =  [45, "vfd", "sdfs", 4, "dfc", 9, "scf"]

j, r = delna(x, y)
print(j, r) #returns ['1', '546', '6']['45', '4', '9']
