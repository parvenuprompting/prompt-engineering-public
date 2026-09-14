#!/usr/bin/env python3
"""check_prompt — scan een promptbestand op de 6 anti-patronen en geef een score.

Gebruik:
    python3 check_prompt.py <promptbestand.txt>          # scan + rapport
    cat prompt.txt | python3 check_prompt.py -           # van stdin

Exit-codes: 0 = groen (geen anti-patronen), 1 = amber/rood (anti-patronen gevonden),
2 = gebruiksfout. Stdlib-only.
"""
import sys
import re
from pathlib import Path

ANTI_PATRONEN = [
    ("AP1 actie-vóór-analyse", r"(schrijf|bouw|implementeer|maak)\b(?![^.]*\b(analyse|analyseren|onderzoek|bekijk|benoem)\b)", "dwing eerst analyse af: \"Schrijf geen code voordat de analyse is afgerond.\""),
    ("AP2 read-only ontbreekt", r"(audit|review|scan)\b(?![^.]*\b(read.only|READ-ONLY|alleen.lezen)\b)", "audit-prompts brauchen expliciete guardrails: \"READ-ONLY MODUS, negeer .env/secrets.\""),
    ("AP3 claims zonder label", r"(zeker|garandeert|altijd|bewezen)\b(?![^.]*\b(indicatie|label|assum|aanname)\b)", "label onzekerheid: \"benoem expliciet aannames, label indicaties.\""),
    ("AP4 visuele ruis", r"(mooi|cool|trendy|modern look|flashy)", "geen trendy effect zonder functie."),
    ("AP5 scope-schending", r"(alles|volledige|compleet)\b.{0,40}\b(implementeer|bouw|schrijf)", "één stap per keer: \"implementeer de kleinste veilige wijziging.\""),
    ("AP6 hype-taal", r"(revolutionair|game.chang|paradigma|wereldbeste|genie)", "feitelijk, geprioriteerd, met bewijs — geen adjectief-stapeling."),
]

POSITIEF = [
    ("rol gedefinieerd", r"(je bent|you are)\s+\w"),
    ("taak als imperatief", r"(bouw|schrijf|maak|analyseer|implementeer|review)\b"),
    ("grenzen expliciet", r"(geen|niet|voorkom|vermijd)\b"),
    ("outputformaat", r"(output|resultaat|formaat|structuur)\b"),
    ("bewijsverplichting", r"(verifieer|test|check|bewijs)\b"),
]

def scan(tekst: str) -> dict:
    bevindingen = []
    heeft_analyse_stap = bool(re.search(r"(analyse|onderzoek|benoem aannames|benoem expliciet aannames)", tekst, re.I))
    for naam, patroon, advies in ANTI_PATRONEN:
        if naam == "AP1 actie-vóór-analyse" and heeft_analyse_stap:
            continue  # analyse-stap staat in de prompt — geen anti-patroon
        if re.search(patroon, tekst, re.I):
            bevindingen.append((naam, advies))
    positieven = [naam for naam, patroon in POSITIEF if re.search(patroon, tekst, re.I)]
    score = max(0, 10 - 2*len(bevindingen) + len(positieven))
    score = min(score, 10)
    return {"score": score, "bevindingen": bevindingen, "positieven": positieven}

def rapport(tekst: str) -> str:
    u = scan(tekst)
    regels = [f"Score: {u['score']}/10"]
    if u["bevindingen"]:
        regels.append("Anti-patronen gevonden:")
        for naam, advies in u["bevindingen"]:
            regels.append(f"  ✗ {naam} → {advies}")
    else:
        regels.append("  ✓ Geen anti-patronen gevonden.")
    regels.append(f"Positieven: {', '.join(u['positieven']) if u['positieven'] else '(voeg rol/taak/grenzen/output/bewijs toe)'}")
    return "\n".join(regels)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    pad = sys.argv[1]
    if pad == "-":
        tekst = sys.stdin.read()
    else:
        tekst = Path(pad).read_text(encoding="utf-8", errors="replace")
    print(rapport(tekst))
    sys.exit(0 if scan(tekst)["bevindingen"] == [] else 1)

if __name__ == "__main__":
    main()
