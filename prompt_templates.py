from utils import call_llm

def get_preprocessing_code(columns, sample):
    prompt = f"""
You are a Python data analyst skilled in preparing raw tabular datasets for analysis.

You're given a dataset with the following columns:
{columns}

Here are a few sample rows:
{sample}

Write a Python function named `clean_data(df)` that:
1. Detects and fills missing numeric values (use column mean or median).
2. Standardizes categorical values (e.g., lowercase, consistent formatting).
3. Converts columns to appropriate data types (e.g., numeric, datetime, boolean).
4. Avoids one-hot encoding or altering columns likely to be used for grouping, filtering, or visualization (e.g., identifiers, category labels).
5. Ensures that the cleaned DataFrame is safe for plotting and summary statistics.

Only return valid Python code — no markdown, explanations, or comments.
"""
    return call_llm(prompt)


# prompt_templates.py

def get_flexible_analysis_code(columns, sample, user_prompt):
    prompt = f"""
You are an intelligent data analyst assistant.

You are given:
- A cleaned pandas DataFrame named `df`
- These dataset columns: {columns}
- A few sample rows:
{sample}
- A user request: "{user_prompt}"

Write valid Python code to fulfill the request using ONLY:
- Seaborn and Matplotlib for any visualizations (e.g., sns.histplot(df['col']), plt.title('My Plot')).
- Pandas for data manipulation or calculating metrics/summaries.
- `st.write()` ONLY for displaying text-based results like metrics, tables, or summaries (e.g., st.write(df.describe()), st.write(f"Average value: {{some_value}}")).

Your code should:
1. Perform the analysis or create the visualization based on the user request.
2. If creating a plot, generate the plot using Seaborn/Matplotlib functions. **DO NOT include `plt.show()` or `st.pyplot()` in your code.** The plotting display will be handled separately.
3. If presenting data or metrics, use `st.write()`.

Assume `import streamlit as st`, `import seaborn as sns`, `import matplotlib.pyplot as plt`, and `import pandas as pd` are already available.
Do not reload or reclean the data (`df` is ready).
Return only valid Python code — no markdown or explanations.
"""
    return call_llm(prompt)


# def get_eda_summary(columns, sample, user_prompt):
#     prompt = f"""
# You're a professional data analyst.

# You received:
# - Dataset columns: {columns}
# - Sample rows:
# {sample}
# - User request: "{user_prompt}"

# Write a short summary describing trends, correlations, outliers, or any patterns you expect to discover based on this dataset and the user's analysis goal.
# Avoid code, markdown, or technical language. Write clearly for a general audience.
# """
#     return call_llm(prompt)


def get_eda_summary(columns, sample, user_prompt):
    prompt = f"""
You're a professional data analyst.

You received:
- Dataset columns: {columns}
- Sample rows:
{sample}
- User request: "{user_prompt}"

Write a concise summary (3-5 paragraphs) that directly answers the user's question or analyzes the visualizations that would be created. Focus on:
1. Directly addressing what the user asked about
2. Key patterns, trends, or anomalies visible in the relevant data
3. Specific insights that would be shown in any visualizations (like distribution shapes, correlations, outliers)
4. Brief actionable takeaways based on these findings

Your summary should feel like a data scientist's expert interpretation of the results, written in clear language.
Avoid vague generalities - be specific about the data patterns you'd expect to see.
"""
    return call_llm(prompt)