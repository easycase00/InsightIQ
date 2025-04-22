import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

def call_llm(prompt, temperature=0.4):
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful Python data science assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=1024
    )
    return response.choices[0].message.content.strip()

def extract_sample(df):
    sample = df.head(5).to_markdown(index=False)
    columns = ", ".join(df.columns.tolist())
    return columns, sample
