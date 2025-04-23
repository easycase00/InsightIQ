# InsightIQ: AI-Powered Data Analysis Platform

## Hosted
**🔗 [Live Demo](https://insightiq000.streamlit.app/)** 

![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Automated-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![LLM](https://img.shields.io/badge/LLM-Integrated-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

InsightIQ is an intelligent data analysis platform that harnesses the power of large language models to automate and enhance the data analysis workflow. This innovative tool bridges the gap between raw data and actionable insights by generating and executing customized data processing and visualization code in real-time.

## Key Features

- **AI-Powered Data Preprocessing**: Automatically detects data types, handles missing values, and standardizes data formats using contextually aware algorithms
- **Intelligent Visualization Generation**: Creates appropriate visualizations based on data characteristics and analysis goals
- **Dynamic Code Generation**: Produces executable Python code tailored to specific analysis requirements
- **Interactive Workflow**: Step-by-step execution of preprocessing and analysis with visual feedback
- **Insight Extraction**: Generates human-readable interpretations of analytical results
- **Responsive UI**: Modern, card-based interface with progress tracking and visual state indicators

## Technical Architecture

### Core Components

The application follows a modular architecture with clear separation of concerns:

1. **Frontend Layer**: Streamlit-based UI with custom CSS for enhanced user experience
2. **LLM Integration Layer**: API interfaces with Groq's LLM services
3. **Data Processing Engine**: Python-based execution environment for generated code
4. **Visualization System**: Matplotlib/Seaborn rendering with buffer management for persistence

### Data Science & ML Implementation Details

#### Adaptive Data Preprocessing

InsightIQ employs sophisticated data preprocessing techniques:

- **Type Inference and Conversion**: Heuristic algorithms detect and convert appropriate data types beyond simple casting
- **Missing Value Imputation**: Context-aware strategies for handling null values (mean/median for numeric, mode for categorical)
- **Categorical Standardization**: Normalization of string values using NLP techniques for consistency

#### Advanced Visualization Strategies

The visualization engine implements:

- **Chart Selection Algorithms**: Automatic determination of optimal visualization types based on data dimensionality and statistical properties
- **Multivariate Analysis**: Correlation detection and appropriate visualization methods for complex relationships
- **Dynamic Parameter Tuning**: Adaptive configuration of visualization parameters based on data characteristics

#### LLM Prompt Engineering

Sophisticated prompt engineering techniques were implemented:

- **Context-Rich Prompting**: Enhancing LLM understanding through structured data representation
- **Task Decomposition**: Breaking complex analytics tasks into manageable sub-problems
- **Output Constraints**: Ensuring consistent, executable code through careful prompt design
- **Temperature Optimization**: Fine-tuned response variability for different generation tasks

#### Memory Management & Execution Safety

- **BytesIO Buffer System**: Efficient in-memory management of visualization artifacts
- **Session State Architecture**: Persistent storage of analysis artifacts across application lifecycle
- **Sandboxed Execution**: Secure code execution within controlled environment variables

## Technical Challenges & Solutions

### Challenge 1: Ensuring Reliable Code Generation

**Solution**: Implemented a robust prompt engineering system with explicit constraints and examples to guide the LLM toward generating executable Python code. Added post-processing cleanup functions to handle common LLM output formatting issues.

### Challenge 2: Maintaining Visualization State

**Solution**: Developed a novel approach using BytesIO buffers and session state management to capture, store, and redisplay matplotlib figures across Streamlit execution contexts, ensuring visualization persistence.

### Challenge 3: Error Handling in Dynamic Code

**Solution**: Created a comprehensive error handling system that captures, logs, and presents exceptions in user-friendly formats while preventing application crashes during dynamic code execution.

### Challenge 4: Cross-Platform Style Consistency

**Solution**: Implemented path-aware StyleLib cleanup to ensure consistent visualization styling across different environments, with intelligent fallback mechanisms.

## Screenshots

### 🔍 User Query and Analysis Plan
![User Query](https://github.com/easycase00/InsightIQ/blob/main/SS/Screenshot%202025-04-22%20at%207.58.28%E2%80%AFPM.png)
*User uploads a CSV, enters a natural language query, and generates an LLM-driven analysis plan.*

### 📊 Auto-Generated Visualizations and Insights
![Visual Output](https://github.com/easycase00/InsightIQ/blob/main/SS/Screenshot%202025-04-22%20at%207.57.15%E2%80%AFPM.png)
*InsightIQ renders plots and written insights based on the user’s query using Seaborn and Matplotlib.*

### 🧼 Cleaned Data and Summary Statistics
![Data Summary](https://github.com/easycase00/InsightIQ/blob/main/SS/Screenshot%202025-04-22%20at%207.59.13%E2%80%AFPM.png)
*Displays cleaned data, inferred column types, and summary statistics automatically.*


## Getting Started

### Prerequisites

- Python 3.8+
- Groq API key

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/insightiq.git
cd insightiq

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env to add your GROQ_API_KEY

# Run the application
streamlit run app.py
```

### Usage
1. Upload a CSV file using the file uploader in the sidebar
2. Enter an analysis query describing what you want to explore
3. Click "Generate Analysis Plan" to create a customized analysis workflow
4. Review and execute the preprocessing step
5. Review and execute the analysis step
6. Examine visualizations and insights

### System Architecture Diagram

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│                 │     │                  │     │                 │
│  Streamlit UI   │◄────┤  InsightIQ Core  │────►│  LLM Service    │
│                 │     │                  │     │  (Groq)         │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                             │       ▲
                             │       │
                             ▼       │
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│                 │     │                  │     │                 │
│  Data Storage   │◄────┤  Code Execution  │────►│  Visualization  │
│  (Pandas)       │     │  Engine          │     │  Engine         │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```
