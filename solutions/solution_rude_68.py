"""Get your act together and spit out all the possible letter combos for the digits 2-9. You know, like how we used to do it on those old-school phones? Ignore any pathetic non-digit trash like ones or zeros; just toss that crap aside. 

Here’s how it works:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, let’s see some examples, because I know you might need them:

Example 1:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a", "b", "c"]

Example 4:
Input: digits = "12*30"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Just to remind you: 
0 <= digits.length <= 4
digits[i] is a digit from '2' to '9'. 

Now get to it! The function you need to write is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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