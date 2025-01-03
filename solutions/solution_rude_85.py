"""Hey genius, you got a string with digits from 2 to 9, right? Well, guess what? Your task is to spit out all the possible letter combos those numbers could represent. And don't even think about leaving out the numbers and letters like a clueless kid. Just stick to the phone button mapping below and filter out any junk like non-digits, ones, or zeros. 

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Now, here's the kicker:  
- If you feed it “23”, you better not come back with anything less than ["ad","ae","af","bd","be","bf","cd","ce","cf"].  
- For an empty string, your output should be as empty as your brain, which is [].
- Got just “2”? Hand over ["a","b","c"] like it's second nature.  
- And if you throw in a mess like "12*30", don't even think about screwing it up – I expect ["ad","ae","af","bd","be","bf","cd","ce","cf"].  

Oh, and remember, the length of your precious digits can’t go over 4. Only the digits between '2' and '9' are welcome here, so keep the other nonsense at bay. 

Now, get to it. The function signature you need is: letterCombinations(digits: str) -> list[str]."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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