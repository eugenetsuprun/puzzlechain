"""Alright, genius, here’s the deal. You’ve got a string packed with digits from 2 to 9, and your pathetic job is to churn out every freakin’ possible letter combination those numbers could represent. You know, like how they did it in the Stone Age with those old-school telephone buttons? Yeah, those. 

Here’s the mapping you should probably memorize if you haven’t already:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and don’t waste my time with any non-digit nonsense. Numbers only, and definitely no ones or zeros. Just filter that junk out.

Got it? Now, here are some examples to help your tiny brain:
1. If the input is "23", you should spit out: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is blank, just give me an empty list: [].
3. For "2", you’d better return: ["a","b","c"].
4. And if you’re faced with "12*30", I expect you to still get: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Keep your constraints in mind while you’re at it: the length of the digits can’t be more than 4, and they must be between '2' and '9'. 

Now, get your act together and write this function: letterCombinations(digits: str) -> list[str]."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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