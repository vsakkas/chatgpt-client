import os

import aiohttp


class ChatGPTClient:
    """
    Client for the unofficial ChatGPT API.
    """

    def __init__(
        self,
        api_key: str | None = None,
        api_base_url: str = "https://api.openai.com/v1/completions",
        suffix: str | None = None,
        max_tokens: int = 2048,
        temperature: float = 0.5,
        top_p: float = 1.0,
        n: int = 1,
        logprobs: int | None = None,
        echo: bool = False,
        stop: str | list[str] | None = None,
        presence_penalty: float = 0.0,
        frequency_penalty: float = 0.0,
        best_of: int = 1,
        logit_bias: dict | None = {},
        user: str | None = "",
    ) -> None:
        """
        Initializes the ChatGPTClient class.

        `api_key` : Optional[str], optional (default: `None`)
            OpenAI API key to authenticate the API request. If not provided, client will use
            `OPENAI_API_KEY` environment variable.

        `api_base_url` : str, optional (default: `"https://api.openai.com/v1/completions"`)
            Base URL for OpenAI API.

        `suffix` : Optional[str], optional (default: `None`)
            The suffix that comes after a completion of inserted text.

        `max_tokens` : int, optional (default: `2048`)
            The maximum number of tokens to generate in the completion.

        `temperature` : float, optional (default: `0.5`)
            Sampling temperature to use. Higher values means the model will take more risks.
            Try 0.9 for more creative applications, and 0 for ones with a well-defined answer.

        `top_p` : float, optional (default: `1`)
            An alternative to sampling with temperature, called nucleus sampling, where the model
            considers the results of the tokens with top_p probability mass. So 0.1 means only the
            tokens comprising the top 10% probability mass are considered. It is generally recommended
            to alter this or temperature but not both.

        `n` : int, optional (default: `1`)
            How many completions to generate for each prompt.
            (Note: Because this parameter generates many completions, it can quickly consume your
            token quota. Use carefully and ensure that you have reasonable settings for max_tokens and stop.)

        `logprobs` : Optional[int], optional (default: `None`)
            Include the log probabilities on the `logprobs` most likely tokens, as well the chosen tokens.
            For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API
            will always return the logprob of the sampled token, so there may be up to `logprobs+1` elements in
            the response.

        `echo` : bool, optional (default: `False`)
            Echo back the prompt in addition to the completion.

        `stop` : Optional[str | list[str]], optional (default: `None`)
            Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain
            the stop sequence.

        `presence_penalty` : float, optional (default: `0`)
            Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear
            in the text so far, increasing the model's likelihood to talk about new topics.

        `frequency_penalty` : float, optional (default: `0`)
            Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency
            in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

        `best_of` : int, optional (default: `1`)
            Generates best_of completions server-side and returns the "best" (the one with the highest
            log probability per token). Results cannot be streamed. When used with n, best_of controls the
            number of candidate completions and n specifies how many to return - best_of must be greater
            (Note: Because this parameter generates many completions, it can quickly consume your token quota.
            Use carefully and ensure that you have reasonable settings for max_tokens and stop.)

        `logit_bias` : Optional[dict], optional (default: `{}`)
            Modify the likelihood of specified tokens appearing in the completion. As an example, you can
            pass {"50256": -100} to prevent the <|endoftext|> token from being generated.

        `user` : Optional[str], optional (default: `""`)
            A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
        """
        # Leaked model name. `text-chat-davinci-002-20230126` is another
        # option, but currently it does not work.
        self._chat_gpt_model = "text-chat-davinci-002-20221122"

        self._api_key = api_key if api_key is not None else os.getenv("OPENAI_API_KEY")
        self._api_base_url = api_base_url

        self._suffix = suffix
        self._max_tokens = max_tokens
        self._temperature = temperature
        self._top_p = top_p
        self._n = n
        self._logprobs = logprobs
        self._echo = echo
        self._stop = stop
        self._presence_penalty = presence_penalty
        self._frequency_penalty = frequency_penalty
        self._best_of = best_of
        self._logit_bias = logit_bias
        self._user = user

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
            "suffix": self._suffix,
            "max_tokens": self._max_tokens,
            "temperature": self._temperature,
            "top_p": self._top_p,
            "n": self._n,
            "logprobs": self._logprobs,
            "echo": self._echo,
            "stop": self._stop,
            "presence_penalty": self._presence_penalty,
            "frequency_penalty": self._frequency_penalty,
            "best_of": self._best_of,
            "logit_bias": self._logit_bias,
            "user": self._user,
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
