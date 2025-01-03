"""Alright, genius, here’s the task: take that string of digits from 2 to 9 and spit out all the letter combos they can make, just like those old-school phone buttons. You know how they work, right? 

Here’s the mapping for your convenience (not that you need it, obviously):

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and if you happen to stumble upon any non-digit junk, like ones or zeros, just toss them out like yesterday’s leftovers. 

Examples? Sure, if you need that extra hand-holding:

1. Input: "23" should spit out: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" gives you nothing. Zip. Nada.
3. Input: "2" should give you: ["a","b","c"]
4. Input: "12*30" should still crank out: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Just remember, the length of your precious digits can’t be over 4, and they better fall between 2 and 9.

Now get to it, and don't waste my time! The function signature you need is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations