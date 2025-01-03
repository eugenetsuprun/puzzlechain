"""Alright, genius, here’s your brain teaser: You’ve got a string of digits (2-9, for those who can count). Your job? Figure out all the letter combos these numbers could possibly generate. And just for kicks, toss out any trash like non-digits, ones, or zeros. 

Here's the mapping, in case you forgot how phones work:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Now, let’s see some examples to really test that brain of yours:

1. Input: "23" — Output should be something like ["ad","ae","af","bd","be","bf","cd","ce","cf"]. 
2. Input: "" — Yeah, you guessed it, [].
3. Input: "2" — Just give me ["a","b","c"].
4. Input: "12*30" — Don’t act surprised, the output should still be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Remember, the function you’re writing is called: `letterCombinations(digits: str) -> list[str]`. Don’t mess it up!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones/zeros
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations