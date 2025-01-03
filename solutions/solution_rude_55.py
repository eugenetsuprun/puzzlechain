"""Alright genius, listen up! You've got this string of digits from 2 to 9, and your job is to churn out every possible letter combo those numbers could represent. Yeah, we’re talking about the old-school phone keypad trick.

Here’s the scoop on what digits map to what letters:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, if you spot any pesky non-digit characters, or zeros, just toss them in the trash. 

Here are a couple of examples to get your brain gears turning:

1. Input: "23" → Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
2. Input: "" → Output: []
3. Input: "2" → Output: ["a", "b", "c"]
4. Input: "12*30" → Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

And just so you know, the digits' length can only be between 0 and 4. Now, get your act together and write this function: letterCombinations(digits: str) -> list[str]. Go!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map.get(digits[index], "")
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(str.isdigit, digits))  # Remove non-digit characters
    backtrack(0, "")
    return combinations