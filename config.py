# -*- coding: utf-8 -*-
import os
from pathlib import Path

DEFAULT_SERVER_HOST = "127.0.0.1"
SERVER_HOST = os.getenv("SERVER_HOST", DEFAULT_SERVER_HOST)
DEFAULT_SERVER_PORT = 12008
SERVER_PORT = int(os.getenv("SERVER_PORT", str(DEFAULT_SERVER_PORT)))

APP_TITLE = "Kimchi Gateway"
APP_DESCRIPTION = "OpenAI-compatible proxy for Kimchi LLM with free credits"
APP_VERSION = "1.0.0"

UPSTREAM_BASE_URL = "https://llm.kimchi.dev/openai/v1"
UPSTREAM_USER_AGENT = "kimchi/0.1.50"

ACCOUNTS_FILE = Path(__file__).resolve().parent / "accounts.json"
LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_FILE = str(LOG_DIR / "gateway.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_ROTATION = "10 MB"
LOG_RETENTION = "7 days"

STREAMING_READ_TIMEOUT = 300.0
CONNECT_TIMEOUT = 30.0

CORS_ORIGINS = ["*"]

MODELS = [
    {"id": "kimi-k2.7", "object": "model", "created": 1700000000, "owned_by": "kimchi", "context_window": 262144, "capabilities": {"vision": True, "tool_use": True, "reasoning": True}},
    {"id": "glm-5.2-fp8", "object": "model", "created": 1700000000, "owned_by": "kimchi", "context_window": 1048576, "capabilities": {"vision": False, "tool_use": True, "reasoning": True}},
    {"id": "deepseek-v4-flash", "object": "model", "created": 1700000000, "owned_by": "kimchi", "context_window": 1048576, "capabilities": {"vision": False, "tool_use": True, "reasoning": True}},
    {"id": "minimax-m3", "object": "model", "created": 1700000000, "owned_by": "kimchi", "context_window": 1048576, "capabilities": {"vision": True, "tool_use": True, "reasoning": True}},
    {"id": "nemotron-3-ultra-fp4", "object": "model", "created": 1700000000, "owned_by": "kimchi", "context_window": 1048576, "capabilities": {"vision": False, "tool_use": True, "reasoning": True}}
]