# Day 2 Analysis

## Part A – Manual ReAct Trace

The problem compares two course-fee options using a 10% and 25% scholarship.

The agent uses two tools:

- `get_course_fee(course_code)`
- `calculator(expression)`

### Reasoning Flow

1. Get the fee of CS101.
2. Get the fee of AI202.
3. Get the fee of DS303.
4. Calculate the cost of CS101 + AI202 after 10% scholarship.
5. Calculate the cost of all three courses after 25% scholarship.
6. Compare both costs.
7. State the cheaper option and difference.

### Result

- Two-course option = ₹27,000
- Three-course option = ₹33,750
- Difference = ₹6,750
- Cheaper option = CS101 + AI202 with 10% scholarship

---

## Part B – Machine ReAct Trace

The `react_trace.py` program was executed using the Day 1 agent.

### Observed Tool Calls

```text
get_course_fee(CS101) → 12000
get_course_fee(AI202) → 18000
get_course_fee(DS303) → 15000

The agent successfully obtained the required course information and produced the correct final comparison.

Paper vs Machine
| Observation                  | Result |
| ---------------------------- | ------ |
| Fee lookup tools used        | Yes    |
| Correct course fees obtained | Yes    |
| Correct final answer         | Yes    |
| Final difference             | ₹6,750 |
| Parallel tool calls          | No     |

Part C – Direct vs Chain-of-Thought

The cot_compare.py program compares direct prompting with Chain-of-Thought prompting.

Three questions were tested:

1.Scholarship and instalment calculation
2.Computer seating calculation
3.Height relationship reasoning
RESULTS
| Question | Direct  | CoT     |
| -------- | ------- | ------- |
| Q1       | Correct | Correct |
| Q2       | Correct | Correct |
| Q3       | Correct | Correct |
The CoT responses were longer because they included step-by-step reasoning and calculations.

Part D – Self-Consistency

The self_consistency.py program runs the same reasoning problem five times with:

Runs = 5
Temperature = 0.8
Observed Answers

The five responses were:

9,562.5
₹9,562.50
9,562.50
₹9,562.5
9562.5 rupees

All five represent the same numerical answer:

₹9,562.50 per instalment
Observation

The model produced different text formats for the same answer. Exact string-based majority voting therefore treated them as different responses, even though they were mathematically equivalent.

Key Observations
ReAct enables the agent to obtain information through tools before answering.
Chain-of-Thought produces more detailed step-by-step responses.
Self-Consistency can produce different response formats for the same answer.
Temperature affects variation between repeated model responses.
Tool use is important when the required information is not directly available to the model.

Conclusion

The Day 2 experiments demonstrated ReAct tool use, Chain-of-Thought reasoning, and Self-Consistency for structured problem solving in Agentic AI.

