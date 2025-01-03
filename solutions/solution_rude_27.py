"""Alright, listen up! You’ve got a string of digits from 2 to 9, and your mission—if you can handle it—is to spit out all the possible letter combinations those numbers could represent. Just like the buttons on an ancient phone, but here’s the kicker: you need to ignore any non-digit nonsense, including ones and zeros. 

Here’s the mapping for your convenience, but don’t expect me to hold your hand:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Now, a few examples in case you need a clue on how to get this done:

1. If you get “23”, your output should be: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If you’re given an empty string, just hand back an empty list: [].
3. If it’s just “2”, keep it simple: ["a","b","c"].
4. And if someone throws “12*30” at you, filter out the trash and still give: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Just remember, the length of your digit string can’t be more than 4. And for heaven's sake, digits can only be between '2' and '9'. 

Now, get on with it! The function signature you need to use is: letterCombinations(digits: str) -> list[str]. Good luck, you’re going to need it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations