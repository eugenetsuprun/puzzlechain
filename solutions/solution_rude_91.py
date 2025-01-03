"""Alright, genius, here’s the deal. You’ve got this string full of digits from 2 to 9, and your pathetic job is to spit out every possible combination of letters those numbers could represent. You know, just like how your phone used to do it before you lost it in the couch cushions.

Here's the mapping you should already know:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

If you see any non-digit nonsense, zeros, or ones, just toss them aside like yesterday’s leftovers.

Let’s look at some examples because clearly, you need them:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a","b","c"]

4. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Now, quit overthinking it and get to coding. Keep it simple and remember, the function signature is: letterCombinations(digits: str) -> list[str]"""

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
    digits = ''.join(filter(str.isdigit, digits))  # Filter out non-digit characters
    digits = ''.join(filter(lambda x: x in phone_map, digits))  # Keep only valid digits
    backtrack(0, "")
    return combinations