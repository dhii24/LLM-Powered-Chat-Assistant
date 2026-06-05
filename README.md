# MiniRAG-AI-Knowledge-Assistant

A simple AI-powered chatbot built using Groq and Llama 3.1 that maintains conversation history and generates context-aware responses.

## Features

* Conversational AI using Llama 3.1
* Persistent chat history during runtime
* Environment variable support using python-dotenv
* Simple command-line interface

## Installation

```bash
git clone <repository-url>
cd MiniRAG-AI-Knowledge-Assistant
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run

```bash
python main.py
```

Type `exit` to quit the chatbot.
