"""Alright, listen up! You’ve got a string full of digits between 2 and 9, and your job is to spit out all the possible letter combos those numbers can give you—just like the junk on old-school phone buttons. Here’s the breakdown:

- 2 gives you ABC
- 3 gives you DEF
- 4 gives you GHI
- 5 gives you JKL
- 6 gives you MNO
- 7 gives you PQRS
- 8 gives you TUV
- 9 gives you WXYZ

Oh, and if there are any non-digit characters, ones, or zeros in the mix? Just toss those out like last week’s leftovers.

Here are some examples to chew on:

1. For digits = "23", you should be able to come up with: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If digits = "", you better just return an empty list—easy enough, right?
3. If digits = "2", the answer should be: ["a", "b", "c"].
4. And if you get digits = "12*30", you still better produce: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Keep in mind: the length of digits can be between 0 and 4, and digits should only be from the range ['2', '9']. 

Now go ahead and write that function: letterCombinations(digits: str) -> list[str]. Don’t screw it up!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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