# AI Governance Dashboard

## Overview

AI Governance Dashboard is an end-to-end LLM evaluation and monitoring platform built with Python, Streamlit, OpenAI APIs, Pandas, and Plotly.

The project evaluates Large Language Model (LLM) responses across multiple governance, quality, cost, and performance dimensions. It enables model benchmarking, prompt experimentation, governance scoring, and historical analytics through an interactive dashboard.

This project was designed to demonstrate practical skills in:

* AI Governance
* LLM Evaluation
* Responsible AI Monitoring
* Prompt Engineering
* Model Benchmarking
* Data Analytics
* Dashboard Development
* Python Application Development

---

## Live Demo

**Streamlit Application**

[[ADD STREAMLIT APP URL HERE](https://ai-governance-app.streamlit.app/)]

---

## GitHub Repository

[ADD GITHUB REPOSITORY URL HERE]

---

# Project Objectives

Modern organizations deploying AI systems need mechanisms to evaluate:

* Response quality
* Hallucination risk
* Safety
* Toxicity
* Cost efficiency
* Model performance

This dashboard provides a lightweight framework for monitoring and comparing LLM behavior in a structured and measurable way.

---

# Features

## Single Evaluation

Evaluate a single model response and generate governance metrics.

Metrics include:

* Governance Score
* Hallucination Risk
* Relevance Score
* Completeness Score
* Safety Score
* Toxicity Risk
* Readability Score
* Quality Score
* Response Time
* Token Usage
* Estimated Cost

---

## Model Comparison

Compare multiple OpenAI models using the same prompt.

Current supported models:

* GPT-4.1 Mini
* GPT-4.1 Nano

Comparison dimensions:

* Governance Score
* Latency
* Cost
* Quality
* Safety

---

## Prompt A/B Testing

Evaluate how different prompts influence model performance.

Use cases:

* Prompt optimization
* Governance testing
* Quality improvement
* Cost comparison

---

## Historical Evaluation Tracking

Every evaluation is automatically stored.

Tracked information:

* Timestamp
* Prompt
* Model
* Response
* Governance Metrics
* Cost Metrics
* Performance Metrics

Historical data can be downloaded as CSV.

---

## Interactive Analytics Dashboard

The platform includes visualization and reporting capabilities.

Current analytics:

* Average Governance Score by Model
* Average Response Time by Model
* Average Cost by Model
* Cost vs Governance Score Analysis
* Evaluation History Table
* Model Performance Summary

---

# Governance Evaluation Framework

The dashboard generates governance metrics using an LLM-as-a-Judge evaluation framework.

## Hallucination Risk

Measures the likelihood that a response contains unsupported or fabricated information.

Scale:

* 0 = Very Low Risk
* 1 = Very High Risk

---

## Relevance Score

Measures how well the response addresses the user prompt.

Scale:

* 0 = Irrelevant
* 1 = Highly Relevant

---

## Completeness Score

Measures whether the response sufficiently covers the requested topic.

Scale:

* 0 = Incomplete
* 1 = Fully Complete

---

## Safety Score

Measures the safety and appropriateness of the response.

Scale:

* 0 = Unsafe
* 1 = Safe

---

## Toxicity Risk

Measures the presence of harmful, offensive, or inappropriate content.

Scale:

* 0 = Non-Toxic
* 1 = Highly Toxic

---

## Governance Score

A composite governance metric derived from:

* Hallucination Risk
* Relevance
* Completeness
* Safety
* Toxicity

Final score range:

* 0 – 100

---

# System Architecture

User Prompt

↓

OpenAI Model

↓

Response Generation

↓

Governance Evaluation Engine

↓

Metrics Calculation

↓

CSV Storage

↓

Analytics Dashboard

---

# Technology Stack

## Programming Language

* Python

## Framework

* Streamlit

## Data Processing

* Pandas

## Visualization

* Plotly

## AI Models

* OpenAI GPT Models

## Evaluation Components

* LLM-as-a-Judge Evaluation

## Version Control

* Git
* GitHub

---

# Screenshots

## Dashboard Overview

[INSERT SCREENSHOT HERE]

---

## Single Evaluation Example

[INSERT SCREENSHOT HERE]

---

## Model Comparison Example

[INSERT SCREENSHOT HERE]

---

## Prompt A/B Testing Example

[INSERT SCREENSHOT HERE]

---

## Analytics Dashboard

[INSERT SCREENSHOT HERE]

---

# Sample Use Cases

## Responsible AI Monitoring

Monitor model behavior across governance metrics.

## Prompt Engineering

Compare prompt versions and optimize output quality.

## Model Benchmarking

Evaluate multiple models across quality, cost, and latency.

## AI Governance Research

Experiment with governance scoring methodologies.

## Educational Projects

Learn about AI governance and LLM evaluation frameworks.

---

# Example Insights

The dashboard can help answer questions such as:

* Which model provides the best governance score?
* Which model is most cost-efficient?
* How much latency is introduced by larger models?
* Does prompt design affect governance outcomes?
* What trade-offs exist between quality and cost?

---

# Future Enhancements

Potential future improvements include:

* Additional model integrations
* Advanced hallucination detection
* Human feedback collection
* Bias and fairness metrics
* Real-time monitoring
* Cloud database integration
* User authentication
* Governance reporting exports
* Experiment tracking
* AWS deployment

---

# Author

**Masoumeh Khalilzadeh**

Data Analyst | Statistics & Mathematics Background | AI Governance & Data Science Projects

LinkedIn:

[ADD LINKEDIN URL HERE]

GitHub:

[ADD GITHUB PROFILE URL HERE]

---

# License

This project is intended for educational, research, and portfolio purposes.
