# The Absurd Clause Contest

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

A make.fun entry for **The Absurd Clause Contest**: one original sentence,
written as an absurd clause that could hide deep inside a terms-of-service
agreement.

## Entry

> By accepting these terms, you consent to the Company renaming your
> firstborn child to a password that meets our complexity requirements.

## Run

```sh
python3 main.py
```

Writes the clause to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`),
then re-reads it byte-for-byte to verify it.
