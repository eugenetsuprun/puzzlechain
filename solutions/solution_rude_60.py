"""Alright, genius, here’s your task: You’ve got a string made up of digits from 2 to 9. Your mission, should you choose to accept it (and I really hope you do because it’s not like you have a choice), is to churn out all the possible letter combinations those digits could represent. And guess what? You can spit out the answer in any order you please. 

Here’s the old-school mapping of digits to letters, just in case you forgot how a telephone works:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

By the way, if your number’s got any non-digit garbage, like ones or zeros, just toss that junk out the window—nobody needs it.

Check out these examples if you need a clue:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And here’s the kicker: keep the length of those digits between 0 and 4, and only deal with digits in the range ['2', '9']. 

Get on it! The function signature you need is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations