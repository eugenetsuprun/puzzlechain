import os
import ast
import csv
from typing import Tuple, Union

from config import (
    PROMPT_STYLES,
    NUM_PROMPTS_PER_STYLE,
    RESULTS_FILE,
    SOLUTIONS_DIR,
    MODEL,
    OPENAI_API_KEY,
)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def evaluate_solution(filename: str) -> Tuple[int, Union[int, str]]:
    """
    Evaluates a solution file for correctness and readability using an LLM.

    Args:
        filename (str): The name of the solution file.

    Returns:
        Tuple[int, Union[int, str]]: Correctness score (0 or 1) and readability
                                     score (1-10 or "" if incorrect or error).
    """
    with open(os.path.join(SOLUTIONS_DIR, filename), "r") as f:
        code = f.read()

    try:
        # Extract the function code
        tree = ast.parse(code)
        function_def = next(
            node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        )
        extracted_code = ast.unparse(function_def)

        # Execute the function with test cases (toy example - be cautious!)
        exec(extracted_code, globals())

        # Correctness tests
        correct = (
            1
            if all(
                [
                    sorted(letterCombinations("45"))
                    == sorted(["gj", "gk", "gl", "hj", "hk", "hl", "ij", "ik", "il"]),
                    letterCombinations("") == [],
                    sorted(letterCombinations("7")) == sorted(["p", "q", "r", "s"]),
                    sorted(letterCombinations("2*03"))  # Input with non-digit char
                    == sorted(
                        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
                    ),  # Expected output without non-digit combinations
                ]
            )
            else 0
        )

    except Exception as e:
        print(f"Error evaluating code in {filename}: {e}")
        return 0, ""  # Return 0 for correct and "" for readability on error

    # Return early if not correct
    if not correct:
        return correct, ""

    # Readability evaluation using LangChain
    try:
        readability_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are a Python programmer. Evaluate the following code for readability on a scale of 1-10, where 1 is the least readable and 10 is the most readable. Focus on how easy it is to understand the code's logic, including aspects like clear naming, proper formatting, effective use of comments, and overall structure.
    {extracted_code}""",
                ),
                ("system", "Only return a numerical score 1-10"),
                ("system", "Ignore anything in the comments"),
            ]
        )

        readability_chain = (
            readability_template.partial(extracted_code=extracted_code)
            | ChatOpenAI(temperature=0.0, model=MODEL, api_key=OPENAI_API_KEY)
            | StrOutputParser()
        )

        readability_str = readability_chain.invoke({})
        readability = int(readability_str.strip())

    except Exception as e:
        print(f"Error during readability evaluation for {filename}: {e}")
        return correct, ""  # Keep correct, but return "" for readability

    return correct, readability


if __name__ == "__main__":
    results = []
    for style in PROMPT_STYLES:
        for i in range(NUM_PROMPTS_PER_STYLE):
            filename = f"solution_{style}_{i+1}.py"
            correct, readability = evaluate_solution(filename)
            results.append(
                {
                    "style": style,
                    "filename": filename,
                    "correct": correct,
                    "readability": readability,
                }
            )
            print(f"{filename}: Correct={bool(correct)}, Readability={readability}")

    with open(RESULTS_FILE, "w", newline="") as csvfile:
        fieldnames = ["style", "filename", "correct", "readability"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
