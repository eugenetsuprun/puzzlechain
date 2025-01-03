"""Alright genius, listen up. You’ve got a string filled with digits from 2 to 9, and your pathetic task is to whip up all the possible letter combos those numbers can spit out. You know, just like what your ancient phone used to do? 

Here’s the breakdown for you, in case you need it spelled out:
- 2 means ABC
- 3 means DEF
- 4 means GHI
- 5 means JKL
- 6 means MNO
- 7 means PQRS
- 8 means TUV
- 9 means WXYZ

Oh, and if you see any non-digit garbage, or those useless '1's and '0's, just toss them aside like the trash they are.

Check out the examples to get your brain going:

1. If you get "23", you should churn out: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. An empty string? Just return an empty list. Duh.
3. "2" should give you: ["a","b","c"]
4. And if you throw in "12*30", well, slice off the junk and still give: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep it simple – digits can only be 0 to 4 characters long and must be from the range '2' to '9'. 

Your function should look like this: letterCombinations(digits: str) -> list[str]. Now go make it happen!"""

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