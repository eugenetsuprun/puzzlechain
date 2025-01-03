"""Alright, listen up! You’ve got a string stuffed with digits 2-9, and your job is to churn out all the possible letter combos that those numbers can represent—like a phone keypad but without the annoying calls. Just ignore any non-digit crap, like ones and zeros, because who needs that nonsense?

Here’s the mapping, in case you can’t remember because you’ve been staring at your phone too much:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Now, don’t screw this up. 

Here are some examples for you to chew on:

1. If the input is "23", you’d better spit out: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If it's empty, just give me []—easy enough, right?
3. If it’s just "2", you better come back with ["a","b","c"].
4. And if you see "12*30", you still need to pull off: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Remember, the constraints are simple: 0 to 4 digits, and they should be in the range of ['2', '9']. 

So, get to it and stop wasting my time! The function signature you need to use is: letterCombinations(digits: str) -> list[str]. Now go and make it happen!"""

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