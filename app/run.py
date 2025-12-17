# -*- coding: utf-8 -*-

from app import create_app
from app.settings.config import DEBUG_MODE


app = create_app()

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, port=5050)
