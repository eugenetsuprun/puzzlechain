"""Alright genius, here’s the deal: You’ve got a string of digits between 2 and 9, and you need to crank out all the possible letter combos those numbers can create. You know, like the ones you dial on your ancient phone. 

Here’s the mapping if you're too lazy to remember:

- Button 2: ABC  
- Button 3: DEF  
- Button 4: GHI  
- Button 5: JKL  
- Button 6: MNO  
- Button 7: PQRS  
- Button 8: TUV  
- Button 9: WXYZ  

Oh, and don’t even think about including any non-digit nonsense, like ones or zeros. Just toss those out like yesterday's garbage.

Check out these examples, in case you need a clue:

1. Input: "23" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" ➔ Output: []
3. Input: "2" ➔ Output: ["a","b","c"]
4. Input: "12*30" ➔ Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And here’s the kicker: the length of your precious digit string can’t go over 4. Got it? Now, get to it! Your function signature is: letterCombinations(digits: str) -> list[str]."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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