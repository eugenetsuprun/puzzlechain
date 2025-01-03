import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inspired by https://leetcode.com/problems/letter-combinations-of-a-phone-number/

CORE_PROMPT = """(Prompt to transform)
Given a string of digits from 2 through 9, return all possible letter combinations that the number could represent (in any order).

Mapping of digits to letters:

Button 2: ABC
Button 3: DEF
Button 4: GHI
Button 5: JKL
Button 6: MNO
Button 7: PQRS
Button 8: TUV
Button 9: WXYZ

The number might have some non-digit characters, ones, or zeros. Filter them out.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:

The length of digits will be between 0 and 4.
digits[i] is a digit in the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]

(End of prompt)
"""

PROMPT_STYLES = ["neutral", "rude", "polite", "URGENT"]
NUM_PROMPTS_PER_STYLE = 100
MODEL = "gpt-4o-mini"
SOLUTIONS_DIR = "solutions"
RESULTS_FILE = "results.csv"
