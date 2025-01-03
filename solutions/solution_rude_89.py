"""Alright, genius, here’s the deal: you’ve got a string of digits from 2 to 9, and your job is to whip up all the possible letter combos that these numbers could spell out. You know, like those old-school phone keypads? Yeah, those.

Here’s the mapping for your reference, but I doubt you need it because you’re a whiz, right?

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and if there are any pesky non-digit characters, or worse—ones and zeros—just toss them in the trash where they belong.

Check out these examples, just in case you need a clue:

1. Input: digits = "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a","b","c"]

4. Input: digits = "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep in mind the rules: your input can be up to 4 digits long, and it better be from the range of '2' to '9'. 

Now, go ahead and craft that function with this signature: `letterCombinations(digits: str) -> list[str]`. Don’t screw it up!"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations