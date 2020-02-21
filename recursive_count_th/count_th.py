'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # define base case
    if len(word) < 2:
        return 0

    # check the first 2 characters for match 'th'
    if word[:2] == 'th':
        # if match return 1 and feed the recursion removing the first letter
        return 1 + count_th(word[1:])
    else:
        # if not match feed the recursion removing the first letter
        return count_th(word[1:])

print(count_th('theth'))
