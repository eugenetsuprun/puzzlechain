"""Alright, genius, here's the deal: you’ve got a string packed with digits between 2 and 9, and your pathetic little job is to whip up all the possible letter combos that those numbers could possibly mean. And do us all a favor, just ignore any garbage - you know, non-digit crap like ones or zeros. 

Here’s the mapping you’re so lucky to have:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, don’t mess this up. If you get an empty input, just return an empty list. If you get something silly like "12*30," filter out the nonsense and get on with it. 

You’ve got constraints too, but let’s not pretend they’re a big deal – just keep the length between 0 and 4. 

Your function should look like this: letterCombinations(digits: str) -> list[str]. So go ahead, give it a shot!"""

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
    
    if len(filtered_digits) == 0 or len(filtered_digits) > 4:
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