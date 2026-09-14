# Gebruik per platform

## Hermes Agent
Plaats `SKILL.md` in je skills-map (`~/.hermes/skills/prompt-engineering/SKILL.md`)
en laad de skill in je agent. De 7 stappen worden dan onderdeel van de agent-flow.

## ChatGPT / Claude (web)
Kopieer de Knowledge- en Steps-secties uit `SKILL.md` als system-prompt bij je
gesprek, en gebruik `check_prompt.py` lokaal om je prompts te scoren vóór je ze
verstuur.

## Lokale tool
```bash
git clone https://github.com/parvenuprompting/prompt-engineering-public
cd prompt-engineering-public
python3 check_prompt.py mijn-prompt.txt
# of van stdin:
cat mijn-prompt.txt | python3 check_prompt.py -
```

## Als Python-package (v1.1, gepland)
```bash
uvx check-prompt mijn-prompt.txt
```
