n8n AI Voice & Telephony Agent

This repository provides a template for building an AI-powered telephony system using n8n, Twilio, and OpenAI. It demonstrates how to handle inbound calls, process speech via LLMs, and respond using TwiML.

Features

Inbound Voice Processing: Uses Twilio Webhooks to capture live audio.

LLM Intelligence: GPT-4o integration for context-aware conversation logic.

STT/TTS Pipeline: Converts customer speech to text and synthesized AI voice back to the caller.

TwiML Orchestration: Generates dynamic XML to control the call flow.

Project Structure

n8n_workflow.json: The core workflow file. Import this into your n8n instance.

custom_enrichment.py: A Python-based TwiML handler for complex logic that exceeds standard n8n node capabilities.

requirements.txt: Python dependencies for the custom handler.

Setup Instructions

n8n Setup:

Import the n8n_workflow.json.

Configure your OpenAI API Credentials.

Twilio Setup:

Buy a Twilio phone number.

Set the Voice URL to your n8n Webhook URL (e.g., https://your-n8n-instance.com/webhook/twilio-voice-inbound).

Environment:

Ensure your n8n instance is accessible via a public URL (use Ngrok for local testing).

Map the SpeechResult body parameter from Twilio to the OpenAI node.

Workflow Visualization

Caller speaks -> Twilio captures audio.

Twilio sends a Webhook with SpeechResult to n8n.

n8n passes text to OpenAI for a response.

n8n formats a TwiML <Say> response.

Twilio reads the response back to the Caller.