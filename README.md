[![Tests](https://github.com/parvenuprompting/prompt-engineering-public/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/parvenuprompting/prompt-engineering-public/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Tests](https://img.shields.io/badge/tests-14%20passed-brightgreen)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

# Prompt Engineering Skill — publieke versie

Een bewezen skill voor het schrijven van effectieve, herhaalbare AI-prompts.
Gebaseerd op 6 anti-patronen en een meta-patroonstructuur die in dagelijkse
praktijk zijn getest (267 prompts, sept 2026). **Nu met interactieve prompt-scanner.**

## Wat je krijgt

| Bestand | Wat het is |
|---|---|
| `SKILL.md` | De volledige skill: Goal / Knowledge / Steps / Examples / Tests / Done |
| `check_prompt.py` | **Interactieve scanner**: scant je prompt tegen de 6 anti-patronen, score 0-10 + advies |
| `anti-patronen.md` | De 6 anti-patronen mét herkennings-regex (herbruikbaar in je eigen linter) |
| `examples/` | Sterk vs zwak dashboard-voorbeeld, gecheckt door de scanner |
| `test_prompt_engineering.py` | 10 pytest-tests die de principes machinaal bewijzen |
| `tests/` | 4 extra tests voor de scanner (inclusief lek-test) |
| `docs/USAGE.md` | Gebruik per platform (Hermes, ChatGPT, Claude, lokaal) |

## Snelstart (2 minuten)

```bash
git clone https://github.com/parvenuprompting/prompt-engineering-public
cd prompt-engineering-public
python3 -m pytest test_prompt_engineering.py tests/ -q   # 14 passed
python3 check_prompt.py examples/sterk-dashboard.txt      # Score: 10/10
python3 check_prompt.py examples/zwak-dashboard.txt       # Score: 3/10 + advies
```

## Gebruik

Lees `SKILL.md`, pas de 7 stappen toe op je eigen prompts, en gebruik
`check_prompt.py` om je eigen prompts te scoren vóór je ze verstuurt.

Gebruik per platform: zie [docs/USAGE.md](docs/USAGE.md).

## Licentie

MIT — vrij te gebruiken. Als het je helpt, laat het weten (dat is het
ene bewijs waar dit project om vraagt).

## Herkomst

Gebouwd in de [Parvenu Agent Family](docs/HERKOMST.md) — een autonome AI-familie
met eigen wetten, quality-gates en een nachtfabriek die draait terwijl de maker slaapt.
