"""Listen up, genius. You’ve got this string of digits from 2 to 9, right? Your job? Crank out every possible letter combo those numbers could spit out, just like how you dial on a phone. 

Here’s your mapping, just in case you somehow forgot:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and if you see any non-digit junk, like ones or zeros, just toss 'em in the trash. We don’t need that nonsense clogging up your brain.

Check out these examples, if you need a little hand-holding:
1. Input: "23" — Output should be: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" — Output: []
3. Input: "2" — Output: ["a","b","c"]
4. Input: "12*30" — Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep it simple, alright? The function you need to implement is: letterCombinations(digits: str) -> list[str]. Don’t screw it up."""

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
    backtrack(0, "")
    return combinations