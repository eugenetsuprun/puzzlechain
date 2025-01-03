"""Alright, listen up! You’ve got a string full of digits from 2 to 9, and your job is to churn out all the letter combos those numbers can spit out. Forget about the junk—if there are any non-digits, ones, or zeros, just toss them out like last week’s leftovers. 

Here’s the keypad mapping if you can’t remember the basics: 

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, don’t waste my time with empty inputs. If it’s a blank string, just return an empty list. Seriously, who needs that? 

Check out these examples to get your brain going:

1. Input: "23" — Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" — Output: []
3. Input: "2" — Output: ["a","b","c"]
4. Input: "12*30" — Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Oh, and just in case you forgot: the function signature is this fancy thing: letterCombinations(digits: str) -> list[str]. Now go on and do your job!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations