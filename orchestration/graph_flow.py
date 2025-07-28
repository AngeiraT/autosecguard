from langgraph.graph import StateGraph, END
from agents.log_monitor_agent import LogMonitorAgent
from agents.triage_agent import TriageAgent
from agents.planner_agent import PlannerAgent
from agents.rl_response_agent import RLResponseAgent

# Agents
log_monitor = LogMonitorAgent([])
triage_agent = TriageAgent()
planner_agent = PlannerAgent()

# Graph node: Detect threats from logs
def detect_threats_node(state):
    logs = state["logs"]
    log_monitor.logs = logs
    threats = log_monitor.detect_threats()
    return {"threats": threats}

# Graph node: Triage each threat
def triage_node(state):
    triaged = []
    for threat in state["threats"]:
        log_message = threat["message"]
        severity = triage_agent.analyze_threat(log_message).strip()
        triaged.append({"log": log_message, "severity": severity})
    return {"triaged_threats": triaged}

# Graph node: Plan response
# def plan_node(state):
#     responses = []
#     for item in state["triaged_threats"]:
#         response = planner_agent.suggest_action(item["log"], item["severity"])
#         responses.append({
#             "log": item["log"],
#             "severity": item["severity"],
#             "response": response.strip()
#         })
#     return {"responses": responses}

rl_agent = RLResponseAgent()

def plan_node(state):
    responses = []
    for item in state["triaged_threats"]:
        action = rl_agent.predict_response(item["severity"])
        responses.append({
            "log": item["log"],
            "severity": item["severity"],
            "response": f"Action: {action}"
        })
    return {"responses": responses}

# Build the LangGraph flow
def build_graph():
    workflow = StateGraph()

    workflow.add_node("detect_threats", detect_threats_node)
    workflow.add_node("triage", triage_node)
    workflow.add_node("plan", plan_node)

    # Transitions
    workflow.set_entry_point("detect_threats")
    workflow.add_edge("detect_threats", "triage")
    workflow.add_edge("triage", "plan")
    workflow.add_edge("plan", END)

    return workflow.compile()
