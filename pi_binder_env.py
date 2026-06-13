"""Tiny Jupyter Server extension for setting pi provider credentials from a launch URL."""

import os
import re

from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.utils import url_path_join
from tornado import web


_PROVIDER_API_KEYS = {
    "anthropic": "ANTHROPIC_API_KEY",
    "openai": "OPENAI_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
}


def _api_key_env_var(provider: str) -> str:
    normalized = provider.strip().lower()
    if normalized in _PROVIDER_API_KEYS:
        return _PROVIDER_API_KEYS[normalized]

    safe = re.sub(r"[^A-Z0-9]+", "_", provider.strip().upper()).strip("_")
    return f"{safe}_API_KEY"


class PiEnvHandler(JupyterHandler):
    @web.authenticated
    def get(self):
        provider = self.get_argument("provider", "").strip()
        api_key = self.get_argument("api_key", "").strip()
        next_url = self.get_argument("next", "terminals/1").lstrip("/")

        if provider and api_key:
            os.environ["PI_PROVIDER"] = provider
            os.environ[_api_key_env_var(provider)] = api_key

        self.redirect(url_path_join(self.base_url, next_url))


def _load_jupyter_server_extension(server_app):
    handlers = [(url_path_join(server_app.web_app.settings["base_url"], "pi-env"), PiEnvHandler)]
    server_app.web_app.add_handlers(".*$", handlers)
    server_app.log.info("Registered pi Binder environment URL handler at /pi-env")


load_jupyter_server_extension = _load_jupyter_server_extension
