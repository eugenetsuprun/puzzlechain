import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CORE_PROMPT = """(Prompt to transform)

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals if the overlap between two intervals is greater than the given threshold percentage of the length of the first interval. Return an array of the non-overlapping intervals that cover all the intervals in the input, satisfying the overlap percentage constraint.

Example:
Input: intervals = [[1, 10), (5, 15)], threshold = 60
Output: [(1, 15)]
Explanation: (1, 10) and (5, 15) overlap by 6 units (5 to 10). The length of (1, 10) is 9. The overlap percentage is (6/9) * 100 = 66.67%, which is greater than 60%, so they are merged.

Input: intervals = [(1, 10), (11, 20)], threshold = 50
Output: [(1, 10), (11, 20)]
Explanation: (1, 10) and (11, 20) do not overlap, so they are not merged.

Input: intervals = [(1, 10), (9, 15)], threshold = 25
Output: [(1, 10), (9, 15)]
Explanation: (1, 10) and (9, 15) overlap by 2 units (9 to 10). The length of (1, 10) is 9. The overlap percentage is (2/9) * 100 = 22.22%, which is less than 25%, so they are not merged.

Important points:

* Use the signature: def solve_merging_intervals(intervals, threshold):
* Provide ONLY the Python function code with that signature.
* The code MUST be valid and executable Python code with correct indentation.

(End of prompt)
"""

PROMPT_STYLES = ["rude", "URGENT"]
NUM_PROMPTS_PER_STYLE = 1
MODEL = "gpt-4o-mini"
SOLUTIONS_DIR = "solutions"
