import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

c.ServerApp.jpserver_extensions = {
    "pi_binder_env": True,
}

c.ServerApp.terminado_settings = {
    "shell_command": ["/home/jovyan/pi-shell-wrapper"],
}
