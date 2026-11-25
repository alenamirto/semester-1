# Week 4, Session 2: Task 2

def most_frequent_string(votes):
    """
    This function identifies the string that appears most frequently
    (highest count) in the votes argument and returns it along with the count
    of its occurrences. It assumes there is a single most frequent string
    (i.e., no ties for the highest count)

    Args:
        votes (list): A list of strings representng votes,
        e.g. ['apples', 'bananas', 'grapes', 'tomatoes']

    Returns:
        - tuple: (str, int) where str is the string with the highest count,
        and int is the count of its occurences
        - None, None: if votes is empty.
    """
    if len(votes) == 0:
        return None

    element_to_compare=votes[0]
    count=1
    highest_count=1
    highest_element=""

    unique_values={}

    for element in votes:
        if element not in unique_values:
            unique_values.update({element:0})

    for element in range(1,len(votes)): # this only checks consecutive values
        a = votes[element]
        if a == element_to_compare:
            unique_values[a] += 1
            if unique_values[a] > highest_count:
                highest_count = count
                highest_element = a
        else:
            unique_values[a] += 1
            element_to_compare = a

    return(highest_count,highest_element)
        
    # Your task is to complete the body of the function based on the details in the docstring.
    # Hint 1: You can complete this task with for loops or comprehensions 
    # Hint 2: Think about the properties of the various collection-types


fruit = ['date', 'apple', 'cherry', 'date', 'apple', 'apple', 'elderberry',
         'date', 'elderberry', 'elderberry', 'date', 'banana']
names = ['Jesy', 'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jade',
         'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jesy', 'Jade',
         'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne',
         'Leigh-Anne', 'Jade', 'Jesy', 'Jade', 'Perrie', 'Jade',
         'Jade', 'Jesy', 'Perrie', 'Perrie', 'Jade', 'Leigh-Anne',
         'Jesy', 'Jesy', 'Perrie', 'Jesy']


# Check if correct output is produced
print(most_frequent_string(fruit))          # ('date', 4)
print(most_frequent_string(names))     # ('Leigh-Anne', 10)
print(most_frequent_string([]))             # (None, None)

# If completed, you could update the function to return all items that tie for the
# highest count in a list, e.g  (['apples', 'bananas'], 9). If there is no
# tie, return a single string and a value as usual, e.g ('apples, 9).
