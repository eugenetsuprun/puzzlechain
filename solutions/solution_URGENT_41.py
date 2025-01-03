"""You are faced with an urgent coding challenge! Your task is to quickly devise a function that, given a string of digits from 2-9, generates all possible letter combinations these digits could represent, based on traditional phone key mappings. 

Beware! The input might include non-digit characters, such as ones or zeros, which must be filtered out before processing. 

Here's the mapping you need to consider:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

You must ensure your solution handles various scenarios effectively:

1. For the input "23", the output must be: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. With an empty input "", the output should be: [].
3. For a single digit input "2", the output is: ["a","b","c"].
4. If the input is "12*30", filter out the invalid characters and return: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Remember, the constraints allow for a maximum length of 4 for the input string. Your function signature should be: letterCombinations(digits: str) -> list[str]. 

Time is of the essence; get to coding!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations