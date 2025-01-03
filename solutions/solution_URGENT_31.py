"""You need to tackle a crucial coding challenge right NOW! The task is to process a string of digits from 2 to 9 and generate all possible letter combinations that correspond to those digits, using the traditional phone keypad mapping. This includes filtering out any non-digit characters, as well as zeros and ones!

Here's the mapping you’ll need to work with:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

**Time is of the essence!** 

You have to implement the function with the following signature: `letterCombinations(digits: str) -> list[str]`

Consider these examples to guide your solution:

1. **Input:** digits = "23"  
   **Expected Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** digits = ""  
   **Expected Output:** []

3. **Input:** digits = "2"  
   **Expected Output:** ["a","b","c"]

4. **Input:** digits = "12*30"  
   **Expected Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Remember!** Constraints dictate that the length of digits should be between 0 and 4. Each digit must be in the range from '2' to '9'. 

You have the power to solve this! Get coding NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only 2-9
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations