"""Alright, listen up! You’ve got this string of digits, only the cool ones from 2 to 9. Your job? Figure out all the possible letter combos those digits can churn out, like the old-school phone keypads. Forget any crap that isn’t a digit — like 0s and 1s or any other junk characters. Just throw 'em in the trash.

Here’s the rundown on what each button has:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Got it? Good. Now, if you get this:

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

Now, make sure you follow the rules, alright? The length of your digits string can be between 0 and 4. Each digit should be in the range of '2' to '9'. 

And for crying out loud, your function needs to be: letterCombinations(digits: str) -> list[str] 

Now go on and make this happen, if you can!"""

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