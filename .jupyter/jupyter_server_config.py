import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

c.ServerApp.jpserver_extensions = {
    "pi_binder_env": True,
}

c.ServerApp.default_url = "/terminals/1"

c.ServerApp.terminado_settings = {
    "shell_command": [
        "/bin/bash",
        "-lc",
        "pi --model openrouter/deepseek/deepseek-v4-pro --approve; exec bash",
    ]
}
