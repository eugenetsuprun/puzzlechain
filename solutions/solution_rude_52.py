"""Alright, listen up! You’ve got a string full of digits between 2 and 9, and your job is to spit out every possible letter combo those numbers can create. Think of it like those old-school phone keypads. 

Here’s the deal:

- Button 2 gives you ABC 
- Button 3 gives you DEF 
- Button 4 gives you GHI 
- Button 5 gives you JKL 
- Button 6 gives you MNO 
- Button 7 gives you PQRS 
- Button 8 gives you TUV 
- Button 9 gives you WXYZ 

And for crying out loud, if there are any unnecessary characters, like letters, ones, or zeros in your string, just toss them out! 

Got it? Now, show me what you can do with these examples:

1. Input: "23" should give you: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" should just give you: []
3. Input: "2" should return: ["a","b","c"]
4. Input: "12*30" should also give you: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember, you’re working with a string of length 0 to 4, and it better only contain digits from '2' to '9'. 

Function signature? Yeah, it’s: letterCombinations(digits: str) -> list[str]. Now go on, make it happen!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters and create a list of valid digits
    valid_digits = [d for d in digits if d in digit_to_letters]
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations