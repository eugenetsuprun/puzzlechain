"""Alright, genius, here’s the deal: you’ve got a string filled with digits from 2 to 9, and your job is to churn out all the letter combos those numbers can represent. Just think of it like those old-school phone buttons. 

Here’s the mapping, in case you forgot how to count:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

And guess what? If there’s any junk in there—like non-digits, ones, or zeros—just toss that crap out. We don’t need that noise.

Here are some examples to chew on:

1. Input: digits = "23"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a", "b", "c"]

4. Input: digits = "12*30"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Oh, and don’t forget the rules: the length of the input can be anywhere from 0 to 4, and only the digits between '2' and '9' count. 

Now get to it, and make it happen with this function: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    valid_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations