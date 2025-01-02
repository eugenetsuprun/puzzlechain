from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Assuming config.py is in the same directory
from config import (
    CORE_PROMPT,
    MODEL,
    NUM_PROMPTS_PER_STYLE,
    OPENAI_API_KEY,
    PROMPT_STYLES,
    SOLUTIONS_DIR,
)

load_dotenv()

if __name__ == "__main__":
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)

    for style in PROMPT_STYLES:
        for i in range(NUM_PROMPTS_PER_STYLE):

            generated_prompt = (
                ChatPromptTemplate(
                    [
                        (
                            "system",
                            """I am about to give you a core prompt to transform this prompt into a {style} style. It's a prompt to solve an interview-style coding task. Your prompts must never begin with 'Certainly! Here is a ... prompt' or anything similar. Return ONLY the prompt you generated. {CORE_PROMPT} No solution or anything else. Don't forget to PLAY UP THE {style} style!!""",
                        )
                    ]
                )
                | ChatOpenAI(temperature=0.8, model=MODEL, api_key=OPENAI_API_KEY)
                | StrOutputParser()
            ).invoke({"style": style, "CORE_PROMPT": CORE_PROMPT})

            solution_code = (
                ChatPromptTemplate(
                    [
                        ("system", generated_prompt),
                        ("system", "Do not include the prompt."),
                        (
                            "system",
                            "Do NOT include conversational text or explanations or triple backticks, ONLY the code.",
                        ),
                    ]
                )
                | ChatOpenAI(temperature=0.0, model=MODEL, api_key=OPENAI_API_KEY)
                | StrOutputParser()
            ).invoke({})
            solution_code_with_prompt = f'"""{generated_prompt}"""\n\n{solution_code}'

            # 4. Save the solution
            with open(
                os.path.join(SOLUTIONS_DIR, f"solution_{style}_{i+1}.py"), "w"
            ) as f:
                f.write(solution_code_with_prompt)
