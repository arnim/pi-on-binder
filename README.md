# 🐍➕📊 MyBinder: Python + R + pi-coding-agent

A ready-to-use [Binder](https://mybinder.org) repository with **Python** and **R**
environments for computational tasks, plus the
[pi-coding-agent](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
preinstalled.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/USER/mybinder-pi-python-r/HEAD)

---

## What's included

| Stack          | Key packages                                                    |
|----------------|-----------------------------------------------------------------|
| **Python 3.11** | numpy, scipy, pandas, matplotlib, seaborn, plotly, scikit-learn, statsmodels, sympy, networkx |
| **R 4.4**       | tidyverse, data.table, caret, randomForest, glmnet, forecast, shiny, rmarkdown, knitr, plotly |
| **Jupyter**     | JupyterLab, classic Notebook, IRkernel, ipykernel               |
| **pi-coding-agent** | CLI coding agent with full tool access (read, write, edit, bash) |
| **pi-kernel**   | Jupyter kernel for pi – talk to pi directly from notebook cells |

---

## 🚀 Launch on MyBinder

Replace `USER` with your GitHub/GitLab username after pushing:

```
https://mybinder.org/v2/gh/<USER>/mybinder-pi-python-r/HEAD
```

Or click the Binder badge above (after updating the URL).

---

## 💻 Local usage

```bash
# Clone the repo
git clone https://github.com/<USER>/mybinder-pi-python-r.git
cd mybinder-pi-python-r

# Recreate the conda environment locally
conda env create -f environment.yml
conda activate pi-python-r

# Install pi-coding-agent (if not done by postBuild)
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# Register Pi kernel
python -m pi_kernel install --user

# Start Jupyter
jupyter lab
```

---

## 🔧 pi-coding-agent quick start

Once the environment is active, run pi from the terminal:

```bash
# Set your API key
export ANTHROPIC_API_KEY=sk-ant-...

# Start interactive mode
pi

# Or non-interactive
pi -p "Analyze the dataset in data.csv"
```

Inside Jupyter, select the **"Pi Agent"** kernel to send notebook cells directly
to pi.

### Pi kernel magics

```
%pi_model anthropic/claude-sonnet-4-5   # switch model
%pi_thinking high                        # set thinking level
%pi_new_session                          # start fresh session
%pi_help                                 # all commands
```

---

## 📁 File overview

```
.
├── environment.yml   ← conda environment (Python + R + Node.js + Jupyter)
├── apt.txt           ← Ubuntu system packages
├── postBuild         ← runs after image build (installs pi)
├── start             ← entrypoint (launches JupyterLab)
└── README.md
```

---

## 📄 License

MIT – use freely for research, teaching, and development.
