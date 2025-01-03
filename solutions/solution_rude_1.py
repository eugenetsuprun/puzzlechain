"""You’ve got a string full of digits from 2 to 9, and your job is to figure out all the possible letter combos these numbers could spit out. Oh, and you better return them however you want, because no one’s judging your style here.

Here’s the breakdown of what each button on the phone does, in case you’ve been living under a rock:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

By the way, if your number has any nonsense characters, 1s, or 0s, just shove those aside like yesterday's trash. 

Here are some examples to help you out (not that you need it):

Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""  
Output: []

Input: digits = "2"  
Output: ["a","b","c"]

Input: digits = "12*30"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And don’t forget the constraints: 

0 <= digits.length <= 4  
Only the digits from '2' to '9' are allowed.

Now, get cracking with this function signature: letterCombinations(digits: str) -> list[str]"""

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