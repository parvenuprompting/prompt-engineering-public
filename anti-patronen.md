# De 6 anti-patronen — met herkennings-regex

Deze patronen komen uit een bewezen praktijk-promptbibliotheek (267 prompts, sept 2026).
Elk patroon heeft de regex die `check_prompt.py` gebruikt — kopieer ze naar je eigen linter.

| # | Anti-patroon | Herkenning (regex) | De fix |
|---|---|---|---|
| 1 | Actie vóór analyse | `(schrijf\|bouw\|implementeer\|maak)\b(?!...analyse...)` | "Schrijf geen code voordat de analyse is afgerond." |
| 2 | Read-only ontbreekt | `(audit\|review\|scan)\b(?!...read.only...)` | "READ-ONLY MODUS; negeer .env/secrets/credentials." |
| 3 | Claims zonder label | `(zeker\|garandeert\|altijd\|bewezen)\b` | "benoem aannames; label indicaties als indicatie." |
| 4 | Visuele ruis | `(mooi\|cool\|trendy\|modern look\|flashy)` | "geen trendy effect zonder functie." |
| 5 | Scope-schending | `(alles\|volledige\|compleet)...(implementeer\|bouw)` | "implementeer de kleinste veilige wijziging." |
| 6 | Hype-taal | `(revolutionair\|game.chang\|paradigma\|wereldbeste\|genie)` | feitelijk, geprioriteerd, met bewijs. |

**De meta-regel erbovenop:** een prompt zonder wanneer/waarvoor/welke-agent is niet
herbruikbaar en niet beoordeelbaar — context is verplicht, niet optioneel.
