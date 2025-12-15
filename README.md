# google-adk-basics
![Static Badge](https://img.shields.io/badge/status-done-brightgreen?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/type-learning_project-blue?style=for-the-badge)

Collection of AI agent projects built with Google ADK (Agent Development Kit) demonstrating multi-agent orchestration, specialized sub-agents, and tool integration for email refinement, financial analysis, and YouTube content creation.

## How to Start

### Environment
- Python 3.13+
- uv (fast Python package manager)
- git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/davidKMJ/google-adk-basics.git
cd google-adk-basics

# Choose a subproject and install dependencies (example: email-refiner-agent)
cd email-refiner-agent
uv sync

# Run the chosen agent
adk web
adk api_server
```

Set required API keys in your environment (e.g., `OPENAI_API_KEY` for LLM access, `FIRECRAWL_API_KEY` for financial-analyst web search) before running agents.

## Key Features
1. **Email Refiner Agent** – Multi-agent loop system that iteratively refines emails through specialized agents (clarity editor, tone stylist, persuasion strategist, synthesizer, and literary critic) until optimization is complete.
2. **Financial Analyst** – Investment advisor agent that coordinates data analysis, financial statement analysis, and news research to provide comprehensive investment advice with generated reports.
3. **YouTube Shorts Maker** – End-to-end content creation pipeline that plans content, generates visual and audio assets, and assembles complete YouTube shorts videos.
4. **Multi-agent orchestration** – Demonstrates Google ADK's LoopAgent and AgentTool patterns for coordinating specialized sub-agents.
5. **Tool integration** – Showcases integration with external APIs (Firecrawl, yfinance) and custom tools for real-world agent capabilities.

## Technical Stack
- **Python 3.13+** – Core runtime for all agent projects
- **uv** – Fast Python package manager and virtualenv management
- **PyProject** – Modern Python project configuration (PEP 621)
- **Google ADK (Agent Development Kit)** – Google's framework for building multi-agent systems with LoopAgent, Agent, and AgentTool orchestration
- **Google Genai** – Google's generative AI SDK for model interactions and artifact management
- **LiteLLM** – Unified interface for multiple LLM providers (OpenAI, Anthropic, etc.) with model abstraction
- **OpenAI SDK** – Direct integration with OpenAI models for advanced function calling and structured outputs
- **Pydantic** – Typed data models and structured outputs for agent responses and validation
- **yfinance** – Yahoo Finance API integration for real-time stock data, financial statements, and market information
- **Firecrawl** – Web scraping and search API for content extraction and real-time web research
- **python-dotenv** – Environment variable management for API keys and configuration
- **aiosqlite** – Async SQLite database support for agent session persistence
- **Jupyter** – Interactive notebook environment for experimentation and development

## Project Structure
```
google-adk-basics/
├── email-refiner-agent/           # Multi-agent email optimization system
│   ├── main.py                    # Entry point (placeholder)
│   ├── deploy.py                  # Vertex AI deployment configuration
│   ├── remote.py                  # Remote agent engine management
│   ├── email_refiner/             # Email refinement agent module
│   │   ├── agent.py               # LoopAgent with clarity, tone, persuasion, synthesizer, and critic sub-agents
│   │   └── prompt.py              # Agent descriptions and instructions
│   ├── travel_advisor_agent/      # Additional travel advisor agent example
│   │   ├── agent.py               # Travel advisor with weather and exchange rate tools
│   │   └── TravelEval.evalset.json # Evaluation dataset
│   ├── api_mode.ipynb             # API mode notebook
│   ├── code_mode.ipynb            # Code mode notebook
│   ├── session.db                 # SQLite session database
│   └── pyproject.toml             # Python 3.13 + Google ADK dependencies
├── financial-analyst/              # Investment advisor with multi-agent analysis
│   ├── main.py                    # Entry point (placeholder)
│   ├── tools.py                   # Firecrawl web search tool
│   ├── financial_advisor/         # Financial advisor agent module
│   │   ├── agent.py               # Main advisor agent coordinating sub-agents
│   │   ├── prompt.py              # Advisor prompts and instructions
│   │   └── sub_agents/            # Specialized analysis agents
│   │       ├── data_analyst.py    # Company info and stock price analysis
│   │       ├── financial_analyst.py # Financial statement analysis (income, balance, cash flow)
│   │       └── new_analyst.py     # News and web research analyst
│   └── pyproject.toml             # Python 3.13 + Google ADK + yfinance + Firecrawl
├── youtube-shorts-maker/          # YouTube Shorts content creation pipeline
│   ├── main.py                    # Entry point (placeholder)
│   ├── youtube_shorts_maker/      # Shorts maker agent module
│   │   ├── agent.py               # Main producer agent with callback hooks
│   │   ├── prompt.py              # Producer prompts and descriptions
│   │   └── sub_agents/            # Content creation pipeline agents
│   │       ├── content_planner/   # Content planning with structured scene output
│   │       ├── asset_generator/   # Image and voice asset generation
│   │       │   ├── image_generator/ # Image generation pipeline
│   │       │   └── voice_generator/ # Voice synthesis tools
│   │       └── video_assembler/   # Final video assembly and composition
│   └── pyproject.toml             # Python 3.13 + Google ADK + OpenAI
└── README.md                      # Project documentation
```

