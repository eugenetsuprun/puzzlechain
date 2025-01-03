"""Alright genius, here's what you need to do: you’ve got a string full of digits from 2 to 9, and your job is to spit out all the possible letter combos that these numbers could represent. Think of it like the old-school phone keypads, but without all the stupid clutter of useless characters like ones and zeros – get rid of those losers.

Here’s the mapping you need to memorize, so you don’t screw this up:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

And just to be clear, if you hit an empty string, don’t even bother returning anything. And if you get something like "12*30", filter out the nonsense and just focus on the digits that actually mean something.

Now, get cracking on this and show me what you’ve got with the function signature: `letterCombinations(digits: str) -> list[str]`. Good luck, you’ll need it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations