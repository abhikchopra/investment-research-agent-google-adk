# Investment Research Agent (Google ADK)

## Overview
Multi-agent investment research system built with Google ADK and Vertex AI.

## Architecture
Planner Agent
Research Agent
Analyst Agent
Writer Agent

## Tech Stack
Google ADK
Gemini 2.5 Flash
Vertex AI
Docker

## Running Locally

source venv/bin/activate
cd ~/Documents
adk web .

## Example Query

Should I invest in Microsoft?

## Running with Docker

Build:

docker build --no-cache -t investment-research-agent-adk .

Run:

docker run -p 8000:8000 
--env-file .env 
-v ~/.config/gcloud:/root/.config/gcloud 
investment-research-agent-adk

Open:

http://localhost:8000

Notes:

* Uses Vertex AI authentication via Application Default Credentials (ADC)
* Requires gcloud auth application-default login
* Mounts local Google credentials into the Docker container
