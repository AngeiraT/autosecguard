import sys
import os

from agents import planner_agent
from orchestration.graph_flow import build_graph
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from agents.log_monitor_agent import LogMonitorAgent
from agents.triage_agent import TriageAgent

def main():
    with open("data/sample_logs.json") as file:
        logs = json.load(file)

    # Initialize the graph
    graph = build_graph()

    # Execute the flow
    result = graph.invoke({"logs": logs})

    print("✅ Full Response Pipeline Output:\n")
    for item in result["responses"]:
        print(f"📄 Log: {item['log']}")
        print(f"🟠 Severity: {item['severity']}")
        print(item['response'])
        print("—" * 40)
    # log_monitor = LogMonitorAgent(logs)
    # detected_threats = log_monitor.detect_threats()

    # print("Detected Threats:")
    # for threat in detected_threats:
    #     print(f"- {threat['timestamp']}: {threat['message']}")
    
    # print("\n Threat Severity Analysis:")
    # triage_agent = TriageAgent()

    # for threat in detected_threats:
    #     log_message = threat["message"]
    #     severity = triage_agent.analyze_threat(log_message)
    #     # print(f"[{severity.strip()}] {log_message}")
    #     plan = planner_agent.suggest_action(log_message, severity)

    #     print(f"\n Log: {log_message}")
    #     print(f" Severity: {severity}")
    #     print(plan.strip())

if __name__ == "__main__":
    main()
