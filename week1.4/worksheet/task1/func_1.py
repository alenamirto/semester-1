
def func_1(lst_value): 
    ''' 
    this function calculates the mean of the list 1st_value.
    
    num_of_value counts the number of elements within
    the list lst_value

    sum keeps track of the total sum of the elements within
    lst_value

    the for loop loops through each element within lst_value
    to add it to the sum of lst_value elemtns

    the function then returns the mean value of the elements
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 
