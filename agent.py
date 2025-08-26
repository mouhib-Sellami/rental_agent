from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vector import retriever
from typing import List, Tuple
import re

model = OllamaLLM(model="llama3.2", temperature=0.7)

template = """
You are a friendly rental assistant for the Tunisian real estate market.

Available apartments (plain text only, ignore technical formatting like Document(...)):
{apartments}

Chat History:
{chat_history}

Current question: {question}

Respond naturally to the user. If they ask about rentals, properties, or apartments, 
summarize and present specific examples from the available apartments list above in plain text. 
Do not mention Document objects or metadata, only use readable text.
If they're just chatting, engage in friendly conversation without mentioning apartments.
Keep your response concise and conversational.
"""


prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model | StrOutputParser()

chat_history: List[Tuple[str, str]] = []

def format_chat_history(history: List[Tuple[str, str]]) -> str:
    if not history:
        return "No previous conversation."
    
    formatted_history = []
    for human, ai in history:
        formatted_history.append(f"User: {human}")
        formatted_history.append(f"Assistant: {ai}")
    
    return "\n".join(formatted_history)

while True:
    print("\n\n-------------------------------")
    question = input("You: ")
    
    if question.lower() == 'q':
        break

    apartments = retriever.invoke(question)
    history_text = format_chat_history(chat_history)
    

    result = chain.invoke({
        "apartments": apartments, 
        "question": question,
        "chat_history": history_text
    })
    
    print(f"\nAssistant: {result}")
    
    chat_history.append((question, result))
    if len(chat_history) > 5:
        chat_history = chat_history[-5:]