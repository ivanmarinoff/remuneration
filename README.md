
# Python Project Template

A low dependency and really simple to start project template for Python Projects.

### What is included on this template?

- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🎯 Entry points to execute your program using `python -m <remuneration>` or `$ remuneration` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.

> Curious about architectural decisions on this template? read [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  

---
# remuneration

[![codecov](https://codecov.io/gh/ivanmarinoff/remuneration/branch/main/graph/badge.svg?token=remuneration_token_here)](https://codecov.io/gh/ivanmarinoff/remuneration)
[![CI](https://github.com/ivanmarinoff/remuneration/actions/workflows/main.yml/badge.svg)](https://github.com/ivanmarinoff/remuneration/actions/workflows/main.yml)

Awesome remuneration created by ivanmarinoff

## Install it from PyPI

```bash
pip install remuneration
```

## Usage

```py
from remuneration import BaseClass
from remuneration import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m remuneration
#or
$ remuneration
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
