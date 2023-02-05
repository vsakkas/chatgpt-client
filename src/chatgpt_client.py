import os
from typing import Optional

import aiohttp


class ChatGPTClient:
    """
    Client for the unofficial ChatGPT API.
    """

    def __init__(
        self,
        api_key: Optional[str],
        api_base_url: str = "https://api.openai.com/v1/completions",
        max_tokens: Optional[int] = 2048,
        temperature: Optional[float] = 0.5,
    ) -> None:
        """
        Initializes the ChatGPTClient class with the following parameters:
        - `api_key`: OpenAI API key to authenticate the API request.
        - `api_base_url`: (optional) Base URL for OpenAI API. Default is `https://api.openai.com/v1/completions`.
        - `max_tokens`: (optional) The maximum number of tokens to generate in the completion. Default is 2048.
        - `temperature`: (optional) What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 for ones with a well-defined answer. Default is 0.5.
        """
        # Leaked model name. `text-chat-davinci-002-20230126` is another
        # option, but currently it does not work.
        self._chat_gpt_model = "text-chat-davinci-002-20221122"

        self._api_key = api_key if api_key is not None else os.getenv("OPENAI_API_KEY")
        self._api_base_url = api_base_url

        self._max_tokens = max_tokens
        self._temperature = temperature

    async def get_completion(self, prompt: str) -> dict:
        """
        Sends a message to OpenAI API for completion and returns the response.
        - `prompt`: Message prompt to be sent to the API.
        """

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._api_key}",
        }
        body = {
            "model": self._chat_gpt_model,
            "prompt": prompt,
            "max_tokens": self._max_tokens,
            "temperature": self._temperature,
            "stream": False,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                self._api_base_url,
                headers=headers,
                json=body,
            ) as response:
                response_json = await response.json()
                return response_json
