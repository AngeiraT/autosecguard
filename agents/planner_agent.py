import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

class PlannerAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0.2)

    def suggest_action(self, log_message: str, severity: str) -> str:
        prompt = f"""
You are an AI cybersecurity responder.

Given the log message:
"{log_message}"

And the assessed severity level: **{severity}**

Decide the best response action from this list:
- Quarantine IP
- Alert security team
- Ignore (benign)
- Initiate password reset
- Block user account
- Isolate system

Then explain briefly **why** this is the correct response.

Respond with:
Action: <recommended action>
Reason: <short explanation>
"""
        return self.llm.invoke(prompt)

