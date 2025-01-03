"""Alright genius, here's the deal: You’ve got a string filled with digits from 2 to 9, and your pathetic job is to churn out all the possible letter combos these numbers could crank out. Don’t get too cozy; just stick to the mapping like you’re supposed to, and leave the junk characters, ones, and zeros in the dust.

Here’s the lowdown on the digits:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Now, if you get something like "23", you better spit out all combos like ["ad","ae","af","bd","be","bf","cd","ce","cf"]. If it’s empty, just give me an empty list, and if it’s a mess with non-digits like "12*30", filter that junk out and still give me the right combos.

Oh, and keep it under control with a 0 to 4 length limit, alright? 

Your function should look like this: letterCombinations(digits: str) -> list[str]. Now go ahead and show me what you got!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    from itertools import product
    
    letter_groups = [digit_to_letters[d] for d in filtered_digits]
    combinations = [''.join(combo) for combo in product(*letter_groups)]
    
    return [combo for combo in combinations if 0 < len(combo) <= 4]