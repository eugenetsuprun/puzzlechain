import pandas as pd
import scipy.stats as stats
from config import RESULTS_FILE  # Assuming you have RESULTS_FILE in your config

# Global constants
GROUP_COL = "style"


def analyze_results(data_file=RESULTS_FILE):
    """
    Loads data from a CSV, performs statistical analysis (Chi-squared and Kruskal-Wallis),
    and prints formatted results.
    """

    df = pd.read_csv(data_file)

    # Ensure 'readability' is numeric where applicable
    df["readability"] = pd.to_numeric(df["readability"], errors="coerce")

    print("Analysis of 'correct' (Correctness):\n")
    print(analyze_correct(df))

    print("\nAnalysis of 'readability' (Readability):\n")
    print(analyze_readability(df))


def analyze_correct(df):
    """Analyzes 'correct' column using Chi-squared test; returns formatted results."""

    contingency_table = pd.crosstab(df[GROUP_COL], df["correct"])
    chi2_stat, p_value, _, _ = stats.chi2_contingency(contingency_table)
    conclusion = (
        "Statistically significant association found (reject H0)"
        if p_value < 0.05
        else "No statistically significant association (fail to reject H0)"
    )

    return f"""Contingency Table:
{contingency_table}

Chi-squared statistic: {chi2_stat:.3f}, p-value: {p_value:.3f}
Conclusion: {conclusion}
"""


def analyze_readability(df):
    """Analyzes 'readability' of *correct only* using descriptive stats and Kruskal-Wallis; returns formatted results."""

    # Filter for correct solutions and valid readability scores
    df_filtered = df[(df["correct"] == 1) & pd.notna(df["readability"])]

    descriptive_stats = str(df_filtered.groupby(GROUP_COL)["readability"].describe())

    # Prepare groups for Kruskal-Wallis
    groups = [
        df_filtered[df_filtered[GROUP_COL] == g]["readability"].tolist()
        for g in df_filtered[GROUP_COL].unique()
    ]

    # Perform Kruskal-Wallis only if there are valid groups with enough data
    if all(len(g) > 1 for g in groups):
        h_stat, p_value = stats.kruskal(*groups)
        conclusion = (
            "Statistically significant difference found (reject H0)"
            if p_value < 0.05
            else "No statistically significant difference (fail to reject H0)"
        )
        kruskal_result = f"""Kruskal-Wallis Results:
H-statistic: {h_stat:.3f}, p-value: {p_value:.3f}
Conclusion: {conclusion}
"""
    else:
        kruskal_result = (
            "Kruskal-Wallis not applicable: Not enough valid data per group."
        )

    return f"""Descriptive Statistics:
{descriptive_stats}

{kruskal_result}
"""


analyze_results()
