"""Alright, genius, here’s the deal. You’ve got a string filled with digits from 2 to 9 and your task is to spit out all possible letter combinations those numbers could stand for. You remember how those old-school phones worked, right? Each number is tied to a bunch of letters like this:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and if your precious number string contains anything that’s not a digit, or has some ones or zeros, just toss those pesky characters out. 

Here are some examples to help your confused brain:

1. For "23", you should get: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. An empty string? Just give back: []
3. If it’s just "2", return: ["a","b","c"]
4. And if it’s "12*30", the result should still be: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Just remember these rules: keep it 0 to 4 digits long, and only deal with digits between 2 and 9. 

Your function needs to be called: letterCombinations(digits: str) -> list[str]. Now, quit screwing around and get it done!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters and keep only digits 2-9
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations