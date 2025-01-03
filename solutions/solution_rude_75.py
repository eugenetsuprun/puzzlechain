"""You’ve got a string full of digits from 2 to 9, and your pathetic job is to dig up all the possible letter combinations these numbers could represent. Yeah, just like those old-school phone buttons. Here’s the mapping for you since you clearly need it spelled out:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, don’t even think about including any non-digit characters, ones, or zeros. Just purge them like they don’t exist!

Here are some examples, in case you can’t figure it out:

Example 1:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a", "b", "c"]

Example 4:
Input: digits = "12*30"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

And by the way, your digits should have a length between 0 and 4, and make sure they’re actually digits from '2' to '9'. 

Get to it: define the function as `letterCombinations(digits: str) -> list[str]` and stop wasting time!"""

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
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations