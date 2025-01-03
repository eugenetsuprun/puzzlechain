"""Alright genius, here's the deal. You’ve got a string filled with digits from 2 to 9 and your task is to spit out all the possible letter combos these numbers could stand for. Think of it like those ancient phone keypads, but way less interesting. 

Here’s the mapping for your tiny brain:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Now, if you find any non-digit crap, or any zeros and ones, just toss them in the trash. 

Check out these examples to figure out how to do your job:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And remember, no more than 4 digits, alright? Keep it simple. You’re writing a function called letterCombinations that takes in a string and returns a list of strings. Don’t screw it up!"""

def letterCombinations(digits):
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    filtered_digits = ''.join([d for d in digits if d in digit_to_char])
    
    if not filtered_digits:
        return []
    
    def backtrack(index, path):
        if index == len(filtered_digits):
            combinations.append(''.join(path))
            return
        
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations