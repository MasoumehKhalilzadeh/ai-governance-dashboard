# AI Governance Dashboard

LLM Evaluation, Monitoring, Benchmarking, and A/B Testing Platform.

## Overview

This project is a Streamlit-based AI governance dashboard that evaluates LLM responses across performance, cost, safety, quality, hallucination risk, relevance, completeness, and overall governance score.

## Features

- OpenAI API integration
- Single response evaluation
- Model comparison
- Prompt A/B testing
- Latency tracking
- Token usage monitoring
- Estimated cost tracking
- Toxicity detection
- Readability scoring
- Hallucination risk evaluation
- Relevance scoring
- Completeness scoring
- Safety scoring
- Overall governance score
- Evaluation history logging
- Trend charts
- CSV export

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Pandas
- Plotly
- Detoxify
- TextStat

## Run Locally

```bash
git clone YOUR_REPO_LINK
cd ai-governance-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py