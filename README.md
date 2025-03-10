# Prompt Engineering Lab

## Project Description

This repository contains the Python source code for exercises related to **Prompt Engineering Lab**.

This project focuses on exploring and practicing basic prompt engineering techniques using **Google Gemini** (as an alternative to OpenAI due to API quota limitations). We implement techniques such as:

*   **Zero-shot Prompting**: Asking a language model to perform a task without any examples.
*   **Few-shot Prompting**: Providing a few examples to guide the language model on how to perform a task.
*   **Chain-of-Thought Prompting**: Encouraging the language model to "think step-by-step" to solve complex problems.
*   **Role Prompting**: Assigning a specific role to the language model to adjust its style and response content.

These exercises are designed to help learners better understand prompt engineering and how to interact effectively with Large Language Models (LLMs) like Gemini.

## Technologies Used

*   **Programming Language**: Python 3.x
*   **Python Libraries**:
    *   `google-generativeai`: Google's official library for interacting with the Gemini API.
    *   `python-dotenv`: For managing API keys and environment variables securely.
*   **Language Model**: Google Gemini Pro (via Google AI Studio)

## Setup and Run Instructions

1.  **Install Python**: Ensure you have Python 3.8 or later installed on your computer. You can download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  **Install Visual Studio Code (Recommended)**: For conveniently writing and running Python code. Download VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).

3.  **Create a Virtual Environment (venv)**:
    *   Open your terminal or command prompt and navigate to the project directory (PromptEngineeringLab).
    *   Run the command: `python -m venv venv`
    *   Activate the virtual environment:
        *   On Windows (CMD): `venv\Scripts\activate`
        *   On macOS/Linux (Bash/Zsh): `source venv/bin/activate`

4.  **Install Required Libraries**:
    *   In the activated virtual environment terminal, run the command: `pip install -r requirements.txt`

5.  **Set up Google Gemini API Key**:
    *   Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create an API key.
    *   Create a `.env` file in the project directory.
    *   Add the following line to the `.env` file, replacing `YOUR_GEMINI_API_KEY` with your created API key:

        ```env
        GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
        ```

6.  **Run Python Files**:
    *   Open a terminal in VS Code (or your activated venv terminal).
    *   To run the zero-shot prompting example, for example: `python zero_shot.py`
    *   Similarly, run other files like `few_shot.py`, `chain_of_thought.py`, `role_prompting.py`, etc.

## Code File Descriptions

*   **`prompt_utils.py`**: Contains utility functions, especially the `send_prompt` function used to send prompts to the Gemini API and receive responses. This function is reused in various exercises.
*   **`test_connection_gemini.py`**: File to test the connection to the Gemini API. Successful execution of this file indicates that the environment and API key are set up correctly.
*   **`zero_shot.py`**: Example of **zero-shot prompting** technique. This file classifies a text passage into different categories without providing examples.
*   **`few_shot.py`**: Example of **few-shot prompting** technique. This file demonstrates how providing a few examples helps Gemini classify text passages more accurately.
*   **`chain_of_thought.py`**: Example of **chain-of-thought prompting** technique. This file solves a simple math problem and requests Gemini to "think step-by-step" to explain the solution process.
*   **`role_prompting.py`**: Example of **role prompting** technique. This file guides Gemini to play the role of a nutrition expert to give dietary advice.
*   **`zero_shot_summary.py`**: Practical example of **zero-shot prompting** for **text summarization** task.
*   **`zero_shot_sentiment.py`**: Practical example of **zero-shot prompting** for **sentiment analysis** task.
*   **`few_shot_active_voice.py`**: Practical example of **few-shot prompting** for **converting passive voice sentences to active voice**.
*   **`few_shot_headline.py`**: Practical example of **few-shot prompting** for **creating catchy newspaper headlines**.
*   **`cot_probability.py`**: Practical example of **chain-of-thought prompting** for **solving probability problems**.
*   **`cot_business_decision.py`**: Practical example of **chain-of-thought prompting** for **business decision analysis**.
*   **`role_prompt_writer.py`**: Practical example of **role prompting** with the role of a **writer** to create the opening paragraph of a short story.
*   **`role_prompt_psychologist.py`**: Practical example of **role prompting** with the role of a **psychologist** to give advice on coping with stress.
*   **`get_role_prompting_definition.py`**: This file is used to **ask Gemini for a definition of "Role prompting"**.
*   **`requirements.txt`**: File listing the required Python libraries for the project.
*   **`.env`**: File containing the Gemini API key (needs to be created and configured separately, do not commit this file to GitHub for API key security).
