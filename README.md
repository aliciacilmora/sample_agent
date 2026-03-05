# Rust-eze Logistics Agent
- Customer-facing AI agent for Rust-eze cargo tracking

# Quick Start
## 1. Clone
```
git clone <your-repo-url>
cd sample_agent
```

## 2. Setup
```
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows
```

## 3. Install
```
pip install -r requirements.txt
```

## 4. Run
```
adk run sample_agent
```

# Test It
```
Track FWD-1013
Aarav Patel orders  
All RTO shipments
```

# Structure
```
sample_agent/
├── __init__.py
├── agent.py       # Rust-eze agent
├── data.py        # Mock shipments DB
└── requirements.txt
```