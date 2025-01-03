"""Alright genius, listen up! You’ve got a string full of digits from 2 to 9, and your pathetic task is to churn out every possible letter combo those numbers could spit out, like they do on those old-school phones. Just ignore any of the useless junk - non-digit nonsense, zeros, and ones - they don’t count. 

Here’s the dumb mapping for your reference:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Now, let’s see if you can manage to churn out the right answers with these examples. 

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

Remember, you’re limited to a measly 4 characters in that string. Get your act together and write the function: letterCombinations(digits: str) -> list[str]."""

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
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations