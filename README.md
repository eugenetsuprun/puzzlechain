# Exploring the Effect of Prompt Style on Code Generation

This project investigates how the style of a coding prompt (neutral, rude, polite, or URGENT) affects the correctness and readability of the code generated by an LLM. I implement an experiment prompting chain using langchain.

[(LinkedIn post)](https://www.linkedin.com/posts/eugenetsuprun_im-learning-an-ai-framework-called-langchain-activity-7280981216156114945-FaQ8?utm_source=share&utm_medium=member_desktop)

## Experiment Overview

1.  **Prompt Generation:** Transform a core coding prompt into different styles: `neutral`, `rude`, `polite`, and `URGENT` and generate some prompts in each style.
2.  **Solution Generation:** Generate Python code solutions for each prompt.
3.  **Evaluation:** Evaluate the correctness (through some quick tests) and readability of each solution (using an LLM).
4.  **Analysis:** Perform statistical analysis (Chi-squared and ANOVA) to determine the impact of prompt style.

# 🚀 Quick Start

Poetry is a dependency management tool for Python. If you don't have it installed, follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Then, run `poetry install`.

Enter the poetry-managed virtual environment with `poetry shell`.

Add an `.env` with your `OPENAI_API_KEY`.

Tweak `config.py`.

Run the scripts in order:

```
python 1_generate_prompts_and_solutions.py
python 2_evaluate_solutions.py
python 3_analyze.py
```

## My Findings

These findings are super limited to the one core prompt I used and the one specific model I used. (`gpt-4o-mini`). Take them with a grain of salt. 🤏

### Correctness

| Style   | Correct % |
| :------ | :-------- |
| URGENT  | 97%       |
| Polite  | 93%       |
| Neutral | 84%       |
| Rude    | 74%       |

This table shows the counts of incorrect and correct solutions for each prompt style.

- **Chi-squared Statistic:** 27.763
- **P-value:** 0.000

**Interpretation:**

🤷‍♂️ It's for a specific model with a specific prompt, so I wouldn't over-interpret here. I think the `rude` ones might have been distracting for the LLM.

### Readability

The generated solutions were pretty similar despite the differences in prompt style. At the readability evaluation step, I asked AI to rate readability on a scale from 1 to 10. My temperature setting was 0. AI rated all 400 as either a 7 or an 8. So I don't think there is anything interesting to report here, even if the Kruskal-Wallis shows significance.

## Repository Structure

```
├── 1_generate_prompts_and_solutions.py
├── 2_evaluate_solutions.py
├── 3_analyze.py
├── config.py
├── results.csv
└── solutions
    ├── solution_polite_1.py
    ├── solution_polite_2.py
    └── ...
```
