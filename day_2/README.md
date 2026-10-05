# Agentic AI – Day 2 Lab

## ReAct, Chain-of-Thought and Self-Consistency

This repository contains the implementation and observations from **Day 2 of the Agentic AI Foundations and Open-Source Practice lab**.

The lab focuses on understanding how an AI agent reasons through a problem using the **ReAct (Reasoning + Acting) cycle**, how **Chain-of-Thought (CoT)** prompting affects reasoning, and how **Self-Consistency** can be used to select an answer through multiple reasoning attempts.

---

## Aim

The main objectives of this lab are:

- Understand the ReAct Thought → Action → Observation cycle.
- Trace an agent's tool usage manually and programmatically.
- Compare direct prompting with Chain-of-Thought prompting.
- Observe whether Chain-of-Thought improves reasoning accuracy.
- Run the same reasoning problem multiple times using Self-Consistency.
- Understand how majority voting can be used to select a final answer.

---

## Prerequisites

The lab uses the environment created during Day 1.

Required:

- Python 3.x
- OpenAI-compatible client
- Groq API access
- Existing Day 1 configuration
- VS Code
- Python virtual environment

The project uses the common `.venv` environment located in the parent `Ai Fluency` folder.

---

## Project Structure

```text
day_2/
│
├── .gitignore
├── README.md
├── analysis.md
├── output/
│   ├── react_trace.png
│   ├── cot_compare.png
│   └── self_consistency.png
│
├── react_trace.py
├── cot_compare.py
└── self_consistency.py
## Part A & B – ReAct

ReAct combines **reasoning and tool use**. The agent follows:

```text
Thought → Action → Observation → Final Answer
The agent uses get_course_fee() to obtain course fees and calculator() for calculations.

Program: react_trace.py

Result:
CS101 + AI202 with a 10% scholarship costs ₹27,000, which is ₹6,750 cheaper than taking all three courses with a 25% scholarship.

Part C – Chain-of-Thought

Chain-of-Thought (CoT) prompting asks the model to solve a problem step by step.

cot_compare.py compares:

Direct prompting
Chain-of-Thought prompting

Three numerical and logical questions are tested to observe differences in correctness and response length.

Part D – Self-Consistency

Self-Consistency runs the same problem multiple times and compares the resulting answers.

Program: self_consistency.py

Configuration:

Runs: 5
Temperature: 0.8

The runs produced different formats of the same numerical answer, ₹9,562.50, showing that equivalent answers can have different text representations.

Key Observations
ReAct: Uses tools to obtain information and perform calculations.
CoT: Encourages step-by-step reasoning.
Self-Consistency: Compares multiple reasoning attempts to identify a common answer.

How to Run

Make sure the common virtual environment is activated from the parent folder:
cd "C:\Users\JAYASRI C\Desktop\Ai Fluency"
.venv\Scripts\activate
Then move into Day 2:

cd day_2
Run the programs individually:

python react_trace.py
python cot_compare.py
python self_consistency.py

Conclusion

This lab demonstrated how ReAct, Chain-of-Thought, and Self-Consistency can improve structured reasoning and tool-based problem solving in Agentic AI systems.
