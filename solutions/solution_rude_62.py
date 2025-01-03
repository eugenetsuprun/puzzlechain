"""Listen up! You got this string of digits from 2 to 9, and your job is to figure out all the possible letter combos those numbers can spit out. So, drop the nonsense and just stick to the numbers, alright? We don’t need your extra junk like non-digit characters or zeros. 

Here’s the deal with the mapping, in case you forgot:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Get it? 

Now, give it a shot. If you mess this up, I don't know what to tell you. 

Example inputs:
- If you throw in "23", the output better be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
- If you try an empty string, then congrats, the output is [].
- Got just "2"? Then you should get ["a","b","c"].
- And for "12*30", chop out the junk and give me ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Just keep it between 0 and 4 digits, and remember, only valid digits from '2' to '9'. 

Your function should look like this: letterCombinations(digits: str) -> list[str]. Now stop wasting time and get on with it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters and create a list of valid digits
    valid_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[valid_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations