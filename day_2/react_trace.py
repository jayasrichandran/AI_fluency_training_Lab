"""Day 2: print the agent's real ReAct trace to compare with your paper trace."""

"""Day 2: print the agent's real ReAct trace to compare with your paper trace."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DAY1_FOLDER = PROJECT_ROOT / "day_1"

sys.path.append(str(PROJECT_ROOT))
sys.path.append(str(DAY1_FOLDER))

from day_1.agent import agent

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

print("QUESTION:", QUESTION, "\n")

print("--- the agent's actions and observations ---")

answer = agent(QUESTION, max_steps=8)

print("\nFINAL ANSWER:", answer)