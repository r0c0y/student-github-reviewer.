from langgraph.graph import StateGraph, START, END
from .state import ReviewState
from .nodes import extract_github_data, code_mentor_review

# 1. Initialize the Graph with our State
builder = StateGraph(ReviewState)

# 2. Add our nodes (the functions we wrote in nodes.py)
builder.add_node("github_extractor", extract_github_data)
builder.add_node("mentor_reviewer", code_mentor_review)

# 3. Define the flow (the edges)
builder.add_edge(START, "github_extractor")
builder.add_edge("github_extractor", "mentor_reviewer")
builder.add_edge("mentor_reviewer", END)

# 4. Compile the graph into an executable app
github_reviewer_app = builder.compile()
