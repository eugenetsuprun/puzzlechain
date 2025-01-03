"""Given a string consisting of digits from 2 to 9, the task is to return all possible letter combinations that the digits could represent, based on the mapping of digits to letters as found on telephone keypads.

The mapping is as follows:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as the digits one or zero. These should be filtered out prior to processing.

Examples for input and expected output:
1. Input: digits = "23" 
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
   
2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a", "b", "c"]

4. Input: digits = "12*30" 
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Constraints to consider:
- The length of the digits string can range from 0 to 4.
- Each character in the string is a digit within the range of ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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