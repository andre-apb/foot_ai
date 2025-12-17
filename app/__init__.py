# -*- coding: utf-8 -*-

import sentry_sdk
from flask import Flask, g
from app.settings.config import DEBUG_MODE, APP_SECRET_KEY, SENTRY_URL
from app.views.api import api_bp

def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Default configuration
    app.config.update(
        SECRET_KEY=APP_SECRET_KEY,
        DEBUG=DEBUG_MODE
    )

    # Override with test configuration if provided
    if test_config is not None:
        app.config.update(test_config)

    # Register blueprints
    app.register_blueprint(api_bp)

    init_sentry()

    return app


def init_sentry():
    if not DEBUG_MODE:
        sentry_sdk.init(dsn=SENTRY_URL, send_default_pii=True, )