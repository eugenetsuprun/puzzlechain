"""Get your act together and figure this out: You’ve got a string of digits from 2 to 9, and your job is to spit out all the possible letter combos those numbers could stand for. You know the deal—these digits map to letters like they do on a phone keypad. 

Here’s the rundown:

- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

Oh, and did I mention? You might find some junk in that string—non-digits, zeros, or ones—so just toss those out like last week’s leftovers.

Check out these examples if you need a clue:

1. Input: "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: "" 
   Output: []

3. Input: "2" 
   Output: ["a","b","c"]

4. Input: "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep it under control with these constraints:

- The string can’t be longer than 4 characters.
- You can only use digits from '2' to '9'.

And your function should look like this: letterCombinations(digits: str) -> list[str]. Now get to work!"""

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