\# Day 3 – Agent Guardrails and Tool Safety



\## Objective



This lab demonstrates how an AI agent uses tools and how guardrails can prevent repeated tool calls when a tool fails to make progress.



\## Files



\- `my\_tools.py` – Tests the calculator and webpage-reading tools.

\- `my\_agent.py` – Basic agent that reads `notice.html` and calculates the fee.

\- `my\_agent\_fixed.py` – Improved agent with a stopping condition for repeated failed tool calls.

\- `notice.html` – Fee notice used by the agent.

\- `big.html` – Large webpage used to test truncated tool output.

\- `make\_big\_page.py` – Generates the large webpage.

\- `output/` – Screenshots of the program outputs.



\## Tool Testing



`my\_tools.py` tests:



\- Course fee calculation

\- Calculator operations

\- Calculator error handling

\- Webpage reading

\- Invalid file handling



Expected fee calculation:



`(12000 + 18000) × 0.9 = ₹27,000`



\## Basic Agent



`my\_agent.py` follows the flow:



Read webpage → Extract information → Calculate → Final answer



For `notice.html`, the agent calculates the total fee for CS101 and AI202 after a 10% merit scholarship as:



\*\*₹27,000\*\*



\## Fixed Agent



`my\_agent\_fixed.py` runs three test questions.



It demonstrates:



1\. Successful webpage reading and calculation.

2\. Stopping after repeated failed tool calls with the same arguments.

3\. Handling a large webpage where the returned content may be truncated.



The stopping condition prevents the agent from repeatedly calling the same failing tool without making progress.



\## Key Observations



\- Tools allow the agent to interact with external information and perform calculations.

\- Invalid tool inputs can produce errors.

\- A basic agent may repeat a failed tool call.

\- A stopping condition prevents unnecessary repeated calls.

\- Large webpage content may be truncated, so the agent must handle incomplete tool output carefully.



\## Result



The Day 3 lab demonstrated tool usage, error handling, repeated-call detection, and stopping conditions for safer and more controlled AI agents.

