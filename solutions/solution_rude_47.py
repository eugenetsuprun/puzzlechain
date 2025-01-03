"""Alright, genius, here's the deal. You’ve got a string filled with digits from 2 to 9, and your task is to spit out all the possible letter combos that these numbers could stand for. You know, like those old-school phone keypads? Yeah, those.

Here’s the mapping, in case you forgot how to read:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Guess what? If you come across any non-digit crap, zeros, or ones, just toss them out. We don’t need that garbage cluttering up your results.

Check out these examples to keep your brain from overheating:

1. Input: "23" – Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" – Output: []
3. Input: "2" – Output: ["a","b","c"]
4. Input: "12*30" – Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Just remember, the length of your precious digits string can be anywhere from 0 to 4, and the digits have to be in the range of 2-9. 

Now, get to it and make that function work: `letterCombinations(digits: str) -> list[str]`. Go on, impress me."""

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