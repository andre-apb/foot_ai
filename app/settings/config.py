# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
from pathlib import Path


# Get the project root directory (where .env should be)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = os.path.join(ROOT_DIR, '.env')

DEBUG_MODE = os.getenv("DEBUG_MODE", "true").lower() in ("true", "1", "yes")
print(f"DEBUG_MODE is {str(DEBUG_MODE)}")


if os.path.exists(ENV_PATH):
    load_dotenv(dotenv_path=ENV_PATH)
    print("Found and loaded .env file")
else:
    print(f"Warning: .env file not found at {ENV_PATH}")

# --- Flask app
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
APP_API_TOKEN = os.getenv('APP_API_TOKEN')

# --- Sentry
SENTRY_URL = os.getenv('SENTRY_URL')

# -- OPEN ROUTER
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
