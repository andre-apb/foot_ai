# -*- coding: utf-8 -*-

import base64
import json
from pathlib import Path

import requests

from app.settings.config import OPENROUTER_API_KEY


class OpenRouterService:
    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self, model: str = "openai/gpt-4o"):
        self.model = model
        self.api_key = OPENROUTER_API_KEY

    def _encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def _get_mime_type(self, image_path: str) -> str:
        suffix = Path(image_path).suffix.lower()
        mime_types = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }
        return mime_types.get(suffix, "image/jpeg")

    def analyze_images(self, prompt: str, image_paths: list[str]) -> dict:
        content = [{"type": "text", "text": prompt}]

        for image_path in image_paths:
            base64_image = self._encode_image(image_path)
            mime_type = self._get_mime_type(image_path)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{mime_type};base64,{base64_image}"
                }
            })

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "response_format": {"type": "json_object"}
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://foot-ai.com",
            "X-Title": "Foot AI"
        }

        response = requests.post(
            self.BASE_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        result = response.json()
        message_content = result["choices"][0]["message"]["content"]

        return json.loads(message_content)
