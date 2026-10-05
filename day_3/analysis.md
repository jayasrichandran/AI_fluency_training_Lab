\# Day 3 – Analysis



\## Part 1: Tool Testing



The `my\_tools.py` program tests the available tools directly.



\### Calculator



The calculator successfully calculates:



```text

(12000 + 18000) × 0.9 = 27000.0

It also rejects invalid expressions and returns:



Calculator error: invalid syntax



This shows that the calculator has input restrictions.



Webpage Reader



The webpage reader successfully reads notice.html.



It also returns an error when a nonexistent file such as no\_such\_file.html is requested.



Part 2: Basic Agent



The my\_agent.py program demonstrates a basic tool-using agent.



For the fee question, the agent performs:



Question

&#x20;  ↓

read\_webpage

&#x20;  ↓

Observation

&#x20;  ↓

calculator

&#x20;  ↓

Observation

&#x20;  ↓

Final Answer



The agent reads the fee notice and calculates:



(12000 + 18000) × 0.9

= 27000



Final answer:



Rs. 27,000

Part 3: Agent Without Guards



The basic agent does not have a protection against repeated failed tool calls.



If the requested file cannot be read, the agent may call the same tool again with the same arguments.



For example:



read\_webpage('fees.html')

read\_webpage('fees.html')



Both calls fail because the requested file is unavailable.



This demonstrates why an agent needs a stopping condition.



Part 4: Fixed Agent and Guardrail



The my\_agent\_fixed.py program adds a guard against repeated tool calls that make no progress.



For the invalid fees.html request, the agent stops after repeated identical failures and produces a message similar to:



Stopped: the tool read\_webpage was called 3 times with the same arguments

and no progress was made.



This prevents the agent from continuing indefinitely.



Part 5: Large Webpage



The big.html test demonstrates handling of a large webpage.



The agent can read the webpage, but the returned content may be truncated.



Therefore, the final answer may be based on the available truncated text or indicate that the page was too long.



Key Observations

Tools allow an agent to perform calculations and retrieve webpage information.

Tools can return errors when invalid inputs or unavailable files are provided.

A basic agent can repeat an unsuccessful tool call.

A stopping condition prevents repeated calls with the same arguments.

Large tool outputs may be truncated and need to be handled carefully.

Conclusion



The Day 3 lab demonstrated tool usage, tool-error handling, repeated-call detection, and stopping conditions. These guardrails make an agent's tool-use loop more controlled and prevent unnecessary repeated actions.





Save and close it.



Then run:



```powershell

dir



You should now have:



day\_3

├── README.md

├── analysis.md

├── my\_agent.py

├── my\_agent\_fixed.py

├── my\_tools.py

├── notice.html

├── big.html

├── make\_big\_page.py

└── output

&#x20;   ├── my\_agent.output.png

&#x20;   ├── my\_agent\_fixed.output.png

&#x20;   └── my\_tools.output.png

