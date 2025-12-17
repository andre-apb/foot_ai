# -*- coding: utf-8 -*-

import json
from pathlib import Path

from app.services.openrouter_service import OpenRouterService


def load_prompt() -> str:
    prompt_path = Path(__file__).parent / "PROMPT.md"
    return prompt_path.read_text()


def main():
    prompt = load_prompt()
    image_paths = [
        "imgs/1.jpeg",
        "imgs/22.jpeg"
    ]

    service = OpenRouterService(model="openai/gpt-4o")
    result = service.analyze_images(prompt, image_paths)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
