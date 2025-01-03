"""Alright, genius, listen up. You’ve got a string that’s supposed to be packed with digits from 2 to 9, and your pathetic job is to spit out all the letter combos these numbers can create. Don’t make it complicated – just think of how those old-school phone buttons worked. 

Here’s the breakdown you should stuff into your brain:

- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

Oh, and don’t even think about letting any useless junk like non-digits, ones, or zeros clutter your output. Just ignore that trash.

Here are some examples to help you grasp this mind-blowing task:

1. If the input is "23", you better output: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If you get an empty input, just return: [].
3. For "2", your output needs to be: ["a","b","c"].
4. And if the input is "12*30", you still stick to the valid digits and give: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Now, keep this in mind: your input length can be anywhere from 0 to 4. And remember, each digit must be from the range of ['2', '9']. 

Your function signature? It’s simple: letterCombinations(digits: str) -> list[str]. Now go and make it happen!"""

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