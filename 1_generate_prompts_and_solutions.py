from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from config import (
    CORE_PROMPT,
    MODEL,
    NUM_PROMPTS_PER_STYLE,
    OPENAI_API_KEY,
    PROMPT_STYLES,
    SOLUTIONS_DIR,
)


def generate_prompt_and_solution(style: str) -> tuple[str, str]:
    """Generates a prompt and solution in the given style."""

    prompt_template = ChatPromptTemplate.from_template(
        "I am about to give you a core prompt to transform into a {style} style. "
        "It's a prompt to solve an interview-style coding task. "
        "Your prompts must never begin with 'Certainly! Here is a ... prompt' or anything similar. "
        "Return ONLY the prompt you generated. No solution or anything else. "
        "Don't forget to PLAY UP THE {style} style!!"
        "Here is the prompt: {CORE_PROMPT}"
    )

    llm = ChatOpenAI(temperature=0.8, model=MODEL, api_key=OPENAI_API_KEY)

    prompt = (prompt_template | llm | StrOutputParser()).invoke(
        {"style": style, "CORE_PROMPT": CORE_PROMPT}
    )

    solution_template = ChatPromptTemplate.from_template(
        "{prompt}\nDo not include the prompt.\n"
        "Do not include conversational text or explanations or triple backticks, ONLY the code starting with a def. "
    )

    llm.temperature = 0.0  # Set temperature for deterministic output
    solution = (solution_template | llm | StrOutputParser()).invoke({"prompt": prompt})

    return prompt, solution


if __name__ == "__main__":
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)

    for style in PROMPT_STYLES:
        for i in range(NUM_PROMPTS_PER_STYLE):
            prompt, solution = generate_prompt_and_solution(style)
            filename = os.path.join(SOLUTIONS_DIR, f"solution_{style}_{i+1}.py")
            with open(filename, "w") as f:
                f.write(f'"""{prompt}"""\n\n{solution}')
