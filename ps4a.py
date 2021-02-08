# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    output = []
    l_output = []
    n = len(sequence) 
    data = list(sequence)
    i = 0
    def permute(data, i, length): 
        if i==length:
            data_copy = data.copy()
            l_output.append(data.copy())
        else: 
            for j in range(i,length): 
                #swap
                data[i], data[j] = data[j], data[i]
                permute(data, i+1, length) 
                data[i], data[j] = data[j], data[i]  

    permute(data, i, n)
    output = [''.join(ele) for ele in l_output]
    
    return(output)

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'aeiou'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)

   
