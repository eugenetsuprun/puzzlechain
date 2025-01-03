"""Alright, genius, here’s the deal: You’ve got some digits from 2 to 9, and you need to figure out all the possible letter combos those numbers can make – just like on those ancient phone keypads. But hey, don’t waste your time with any of that non-digit nonsense, like ones or zeros. Just kick 'em to the curb.

Here’s the mapping for your precious buttons:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Now get this straight: if the input is empty, you’re just going to return an empty list. If it’s something like "23," then you better cough up all those combinations like ["ad","ae","af","bd","be","bf","cd","ce","cf"]. And if it's a mess like "12*30," chop out the junk and give me those valid combos.

Here’s your function signature to work with: letterCombinations(digits: str) -> list[str]. Now stop dilly-dallying and get to it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # Filter out invalid characters
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations