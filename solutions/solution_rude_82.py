"""Alright genius, listen up. You’ve got a string full of digits from 2 to 9, and your job is to whip up all the possible letter combinations that those digits could spit out. Just like those old-school phone keypads. 

Here’s the breakdown for you:

- Button 2 gives you ABC
- Button 3 gives you DEF
- Button 4 gives you GHI
- Button 5 gives you JKL
- Button 6 gives you MNO
- Button 7 gives you PQRS
- Button 8 gives you TUV
- Button 9 gives you WXYZ

Oh, and don’t forget that the number might be cluttered with junk like non-digits, ones, or zeros. Just toss them in the trash.

Now, let’s see some examples to clarify, since I know you might need it:

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

Just keep it in your head: 
- Constraints: 0 <= digits.length <= 4, and every digit must be between '2' and '9'.

Now go ahead and write that function: letterCombinations(digits: str) -> list[str]. Don’t screw it up!"""

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
           