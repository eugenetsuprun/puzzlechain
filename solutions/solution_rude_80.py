"""Alright genius, here’s your task. You’ve got a string of digits from 2 to 9, and your job is to spit out all the possible letter combos those numbers could represent. Yeah, just like those old-school phone buttons. 

Here’s the mapping in case you forgot how the world works:  
Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and don’t waste my time with any non-digit nonsense, like ones or zeros. Just get rid of them, alright? 

Here are some examples to help you not screw it up:  
Input: digits = "23" should give you ["ad","ae","af","bd","be","bf","cd","ce","cf"].  
Input: digits = ""? Yeah, that’s just an empty list: [].  
Input: digits = "2" gives you ["a","b","c"].  
Input: digits = "12*30"? You should end up with ["ad","ae","af","bd","be","bf","cd","ce","cf"].

And here are the constraints you have to follow, since apparently that’s needed:  
0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

Try to keep up. The function signature is: letterCombinations(digits: str) -> list[str]. Now get to it!"""

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