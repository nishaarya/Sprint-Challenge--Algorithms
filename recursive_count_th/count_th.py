'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    counter = 0

    pass

    # if not equal to 'th'
    if word == "":
        return 0
    # if equal to 'th'
    elif word[:2] == 'th':
        # +1 on the counter (old count + 1)
        counter += 1
        return count_th(word[1:]) + counter
    else:
        return count_th(word[1:])
