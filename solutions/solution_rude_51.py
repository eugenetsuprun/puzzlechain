"""Alright, listen up. You’ve got a string of digits from 2 to 9, and your job is to crank out every possible letter combo those numbers can spawn. It’s like the old phone keypads, capisce? Here’s the deal: 

- 2 maps to ABC 
- 3 to DEF 
- 4 to GHI 
- 5 to JKL 
- 6 to MNO 
- 7 to PQRS 
- 8 to TUV 
- 9 to WXYZ 

Don’t even think about including anything not a digit, or ones and zeros – they’re just junk, so toss ‘em. 

Oh, and by the way, here are some examples to help you along:

1. Input: "23" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" Output: [] 
3. Input: "2" Output: ["a","b","c"]
4. Input: "12*30" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Your constraints? Keep it simple: the length is between 0 and 4, and only the digits between '2' and '9' are allowed. 

Now get to it, and make sure you nail that function signature: letterCombinations(digits: str) -> list[str]. No slacking off!"""

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