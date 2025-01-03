"""Alright genius, here's the deal: you've got this string with digits from 2-9, and your job is to whip up all the possible letter combos those numbers could stand for. You know, like back in the day when phones had buttons for letters. 

Here’s the mapping for your convenience, in case you forgot how to read:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and if you spot any pesky non-digit characters, zeroes, or ones in there, just toss them out like yesterday’s leftovers. 

Here’s how you might want to tackle it:

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

You’ve got some constraints to follow: 0 <= digits.length <= 4 and digits[i] has to be a digit from '2' to '9'. 

Now, quit wasting time and get this done. The function signature looks like this: letterCombinations(digits: str) -> list[str]. Good luck, you'll need it!"""

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