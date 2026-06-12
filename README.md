# 🐍➕📊 MyBinder: Python + R + pi-coding-agent

A ready-to-use [Binder](https://mybinder.org) repository with **Python** and **R**
environments for computational tasks, plus the
[pi-coding-agent](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
preinstalled.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD?urlpath=%2Fdoc%2Ftree%2Findex.ipynb)

---

## What's included

| Stack          | Key packages                                                    |
|----------------|-----------------------------------------------------------------|
| **Python 3.11** | numpy, scipy, pandas, matplotlib, seaborn, plotly, scikit-learn, statsmodels, sympy, networkx |
| **R 4.4**       | tidyverse, data.table, caret, randomForest, glmnet, forecast, shiny, rmarkdown, knitr, plotly |
| **Jupyter**     | JupyterLab, classic Notebook, IRkernel, ipykernel               |
| **pi-coding-agent** | CLI coding agent with full tool access (read, write, edit, bash) |

---

## 📓 Quick tour

Open **`index.ipynb`** after launch — it walks through Python, R, and
pi-coding-agent with ready-to-run cells.

## 🚀 Launch on MyBinder

Click the Binder badge above, or visit:

```
https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD?urlpath=%2Fdoc%2Ftree%2Findex.ipynb
```

### Launch with a pi API key

URL-encode your key, then launch via `pi-env`:

```text
OpenAI:     https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD?urlpath=pi-env%3Fprovider%3Dopenai%26api_key%3DYOUR_KEY
Anthropic:  https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD?urlpath=pi-env%3Fprovider%3Danthropic%26api_key%3DYOUR_KEY
OpenRouter: https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD?urlpath=pi-env%3Fprovider%3Dopenrouter%26api_key%3DYOUR_KEY
```

This sets `PI_PROVIDER` plus the matching `*_API_KEY` for the session. Do not share URLs containing real keys.

---

## 💻 Local usage

```bash
# Clone the repo
git clone https://github.com/yfiua/pi-on-binder.git
cd pi-on-binder

# Recreate the conda environment locally
conda env create -f environment.yml
conda activate pi-python-r

# Install pi-coding-agent (if not done by postBuild)
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

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

---

## 📁 File overview

```
.
├── environment.yml   ← conda environment (Python + R + Node.js + Jupyter)
├── apt.txt           ← Ubuntu system packages
├── postBuild         ← runs after image build (installs pi)
├── index.ipynb       ← quick-start walkthrough notebook
└── README.md
```

## 📄 License

MIT – use freely for research, teaching, and development.
