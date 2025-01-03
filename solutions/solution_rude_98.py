"""Alright, listen up. You’ve got a string filled with digits from 2 to 9, and your pathetic job is to churn out all the possible letter combos that these numbers can represent. Just like those old-fashioned phone keypads, you know? 

Here’s the breakdown of the buttons, in case you somehow forgot:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

And hey, if there are any pesky non-digit characters, ones, or zeros in your precious input, just toss them out like the garbage they are.

Now, here's what you’re dealing with:

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

And don’t forget the constraints:  
0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

So get your act together and make that function: letterCombinations(digits: str) -> list[str]. """

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
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations