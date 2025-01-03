from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

from config import (
    CORE_PROMPT,
    MODEL,
    NUM_PROMPTS_PER_STYLE,
    OPENAI_API_KEY,
    PROMPT_STYLES,
    SOLUTIONS_DIR,
)

load_dotenv()


def save_solution(prompt: str, code: str):
    solution_code_with_prompt = f'"""{prompt}"""\n\n{code}'
    with open(os.path.join(SOLUTIONS_DIR, f"solution_{style}_{i+1}.py"), "w") as f:
        f.write(solution_code_with_prompt)


def get_prompt(style: str) -> str:
    """Get a prompt for the given style."""
    template = ChatPromptTemplate(
        [
            (
                "system",
                "I am about to give you a core prompt to transform into a {style} style. It's a prompt to solve an interview-style coding task. Your prompts must never begin with 'Certainly! Here is a ... prompt' or anything similar. Return ONLY the prompt you generated. {CORE_PROMPT} No solution or anything else. Don't forget to PLAY UP THE {style} style!!",
            )
        ]
    )

    return (
        template
        | ChatOpenAI(temperature=0.8, model=MODEL, api_key=OPENAI_API_KEY)
        | StrOutputParser()
    ).invoke({"style": style, "CORE_PROMPT": CORE_PROMPT})


def get_solution(prompt: str) -> str:
    """Get the solution code for the given prompt."""
    return (
        ChatPromptTemplate(
            [
                ("system", prompt),
                ("system", "Do not include the prompt."),
                (
                    "system",
                    "Do NOT include conversational text or explanations or triple backticks, ONLY the code. Do not include the command to run python.",
                ),
            ]
        )
        | ChatOpenAI(temperature=0.0, model=MODEL, api_key=OPENAI_API_KEY)
        | StrOutputParser()
    ).invoke({})


if __name__ == "__main__":
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)

    for style in PROMPT_STYLES:
        for i in range(NUM_PROMPTS_PER_STYLE):

            generated_prompt = get_prompt(style)
            solution_code = get_solution(generated_prompt)
            save_solution(generated_prompt, solution_code)
