"""You think you can handle this? Alright, here’s the deal: you’ve got a string full of useless digits from 2-9, and your precious task is to spit out every possible letter combo that these numbers can represent. But don’t get too comfy; if there are any non-digit distractions, just toss them aside like yesterday's leftovers.

Here’s your pathetic little map for reference:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Yeah, the number could have a bunch of junk characters, ones, or zeros—who cares? Just filter that nonsense out.

Check out these examples to see what I mean:

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

Just remember, you’ve got constraints here: 

0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

Your function signature? Yeah, it’s just this: letterCombinations(digits: str) -> list[str]. 

Now go on, get it done!"""

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