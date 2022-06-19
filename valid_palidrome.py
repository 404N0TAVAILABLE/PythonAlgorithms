# Given a non-empty string c, you may delete at most one character.  Judge
# whether you can make it a palidrome.
# The string will only contain lowercase characters a-z
#

import enchant

d = enchant.Dict("en_US")

c = 'radkar'
def solution(c):
    for g in range(len(c)):
        t = c[:g] + c[g + 1:]
        print(f'--> c : {c[:g]}')
        print(f'c + 1 : {c[g + 1:]}')
        print(f't is : {t}')
        print(f'if t == {t[::-1]}')
        # check if word is a palidrome and a valid word
        if t == t[::-1] and d.check(t): 
            print(f'{c} can be made into a palidrome : {t}')
            return True

    return c == c[::-1]

if not (solution(c)): print(f'{c} cannot be made into a palidrome')
