"""Got a string full of digits from 2 to 9? Great, now go ahead and spit out all the possible letter combos those numbers can create. You know, like those silly buttons on a phone? Yeah, those. 

Here's the mapping you should care about:
- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

Oh, and if you've thrown in any non-digits, ones, or zeros, just toss those out like yesterday's trash. 

Check out these examples to get your head wrapped around it:

1. Input: "23" - Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
2. Input: "" - Output: []
3. Input: "2" - Output: ["a", "b", "c"]
4. Input: "12*30" - Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

You’ve got some constraints to keep in mind: the length of your digits string should fall between 0 and 4, and those characters must be in the range of '2' to '9'. 

Now, get to it! The function you need is: letterCombinations(digits: str) -> list[str]. Don’t screw it up!"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations