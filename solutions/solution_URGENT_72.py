"""**URGENT: STAT!** You need to implement a function to decode a string of digits (only 2-9), representing letters on a phone keypad. Your task is critical: return all potential letter combinations these digits could create, filtering out any non-digit characters immediately! 

Here’s what you’re dealing with:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

**Make sure to handle edge cases:**
- An empty string should return an empty list.
- Ignore characters like ones or zeros - they don’t contribute!

**Examples:**
1. Input: "23" should yield combinations like ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. Input: "" should yield [].
3. Input: "2" should yield ["a", "b", "c"].
4. Input: "12*30" should also yield ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

**GO! The function signature you need to follow is:**
```python
def letterCombinations(digits: str) -> list[str]:
``` 

Time is of the essence! Get to it NOW!"""

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