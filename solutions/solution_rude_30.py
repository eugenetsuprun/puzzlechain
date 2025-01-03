"""Alright genius, listen up. You’ve got a string packed with digits from 2 to 9, and your oh-so-important mission is to whip up all the possible letter combos that this number could stand for. Yeah, you heard me right. And just to make it extra clear, here’s the dumbed-down version of how the digits map to letters, like those ancient telephone buttons:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and if you see any non-digit junk, zeros, or ones in there? Good news! You can just kick them to the curb. 

Here’s what you need to produce:

- Input: A string of digits, maybe even some trash.
- Output: A list of all the letter combinations. 

To help you visualize, here are some examples, even though I’m sure you can handle it:

1. Input: "23" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" → Output: []
3. Input: "2" → Output: ["a","b","c"]
4. Input: "12*30" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep it concise: 0 to 4 digits, and those digits better be between '2' and '9'. 

Now get cracking on the function: `letterCombinations(digits: str) -> list[str]`. Don’t screw this up!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
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