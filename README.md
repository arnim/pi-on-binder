# pi-on-binder

A ready-to-use [Binder](https://mybinder.org) repository with preinstalled [pi-coding-agent](https://www.npmjs.com/package/@earendil-works/pi-coding-agent), **Python** and **R**
environments for computational tasks.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD)

---

## What's included

| Stack          | Key packages                                                    |
|----------------|-----------------------------------------------------------------|
| **pi-coding-agent** | CLI coding agent with full tool access (read, write, edit, bash) |
| **Python 3.11** | numpy, scipy, pandas, matplotlib, seaborn, plotly, scikit-learn, statsmodels, sympy, networkx |
| **R 4.4**       | tidyverse, data.table, caret, randomForest, glmnet, forecast, shiny, rmarkdown, knitr, plotly |
| **Jupyter**     | JupyterLab, classic Notebook, IRkernel, ipykernel               |


---

## 📓 Quick tour

Open **`index.ipynb`** after launch — it walks through Python, R, and
pi-coding-agent with ready-to-run cells.

## 🚀 Launch on MyBinder

Click the Binder badge above, or visit:

```
https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD
```

### Launch with an OpenRouter API key

URL-encode your key, then launch via `pi-env`:

```text
https://mybinder.org/v2/gh/yfiua/pi-on-binder/HEAD?urlpath=pi-env&provider=openrouter&api_key=YOUR_KEY
```

This sets `PI_PROVIDER` plus the matching `*_API_KEY` for the session, opens a terminal, and starts `pi --model openrouter/deepseek/deepseek-v4-pro --approve` automatically.
Do not share URLs containing real keys.

---

### Launch pi from the JupyterLab launcher

After launch, click the **Pi Agent** icon (with the pi logo) in the launcher.
It opens a terminal and runs pi with `pi --model openrouter/deepseek/deepseek-v4-pro --approve` automatically.

Alternatively, open a terminal and type `pi`.

---

## 📄 License

MIT – use freely for research, teaching, and development.
