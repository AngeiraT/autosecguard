# 🔐 AutoSecGuard

Multi-agent cybersecurity framework using LLMs and Reinforcement Learning.

## 🚀 Quick Start

## 📁 Project Structure

```text
autosecguard/
├── .env
├── .env.example
├── .git/
├── .gitignore
├── .qodo/
├── README.md
├── requirements.txt
├── agents/
│   ├── __init__.py
│   ├── log_monitor_agent.py
│   ├── planner_agent.py
│   ├── rl/
│   │   ├── response_env.py
│   │   └── train_rl_agent.py
│   ├── rl_response_agent.py
│   └── triage_agent.py
├── data/
│   ├── sample_logs.json
│   ├── supervised_threats.json
│   └── threat_intel.json
├── orchestration/
│   ├── graph_flow.py
│   └── main_flow.py
├── tests/
├── utils/
│   └── threat_score.py
├── venv/
```

```bash
# Clone and install
git clone https://github.com/yourname/autosecguard.git
cd autosecguard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run main agent logic
python orchestration/main_flow.py
