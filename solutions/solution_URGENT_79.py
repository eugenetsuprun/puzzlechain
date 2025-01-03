"""URGENT: You need to tackle this coding task IMMEDIATELY! Given a string of digits from 2-9, your mission is to return ALL possible letter combinations that these numbers can represent, similar to the mappings on old telephone keypads. 

Here’s the mapping you must use:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: Filter out any non-digit characters, including zeros and ones. 

You must handle the following scenarios with extreme precision:

1. Input: "23" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" should yield Output: []
3. Input: "2" should yield Output: ["a","b","c"]
4. Input: "12*30" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember, the function signature is: letterCombinations(digits: str) -> list[str]. 

Time is of the essence! Get to work!"""

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