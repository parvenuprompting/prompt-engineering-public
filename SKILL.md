# Skill: Prompt Engineering

## Goal

Effectieve, herhaalbare prompts schrijven voor LLM's en agents: rol + taak + grenzen expliciet vastleggen, output structureren, en anti-patronen vermijden. Eindtoestand: je kunt zonder externe hulp een prompt bouwen die voorspelbare, geverifieerbare output levert — en je kunt een zwakke prompt systematisch diagnoséren en verbeteren.

**Niet-doel:** prompt-injectie-verdediging (aparte security-skill), tool-gebruik/MCP-architectuur, fine-tuning.

## Knowledge

Deze kennis komt rechtstreeks uit een bewezen praktijk-promptbibliotheek (267 prompts, sept 2026):

- **Structuur wint van inspirationaliteit.** Een werkende prompt heeft vaste onderdelen: rol ("Je bent een senior software engineer"), taak (exact wat), context (waarvoor, welke omgeving), grenzen (wat NIET), outputformaat. Inspiratie-teksten ("je bent een genie") leveren niks meetbaars op.
- **De 6 anti-patronen** (uit `prompts/anti-patronen.md` — de bewezen standaard):
  1. **Geen actie vóór analyse** — dwing altijd eerst analyse af: "Schrijf geen code voordat de analyse is afgerond."
  2. **Read-only audits zonder uitzondering** — expliciete guardrails: "READ-ONLY MODUS", "negeer .env/secrets/credentials".
  3. **Geen claims zonder label** — "label statistische claims expliciet als indicatie, niet geverifieerd". Geen harde garanties.
  4. **Geen visuele ruis, geen trendeffecten** — "geen trendy effect zonder functie".
  5. **Geen scope-schendingen** — één stap per keer; "implementeer de kleinste veilige wijziging"; geen tijdsschattingen tenzij gevraagd.
  6. **Geen hype in taal** — geen "revolutionair", geen adjectief-stapeling; feitelijk, geprioriteerd, met bewijs.
- **Bewijsnorm in de prompt zelf.** "Done" = geverifieerd met echte output, nooit aangenomen — bouw dat eis in: "verifieer je bevindingen tegen de codebase, verwijs naar bestandsnamen en regels."
- **Placeholders gemarkeerd en herbruikbaar:** `<ONDERWERP>`, `[BESCHRIJVING]` — nooit verwarren met letterlijke tekst.
- **Context is verplicht, niet optioneel.** Een prompt zonder wanneer/waarvoor/welke agent kan niet hergebruikt of beoordeeld worden.
- **Kwaliteit boven kwantiteit:** een prompt die niet meer werkt, wordt gemarkeerd als `[VEROUDERD]` — niet weggegooid, niet stil blijft staan.
- **LLM's hallucineren bij open vragen.** Verplicht explicititeit: "benoem expliciet gemaakte aannames", "prioriteer alleen concrete issues".

## Steps

1. **Definieer het doel in één zin.** Wat moet de output zijn en waaraan merk je dat het goed is? (Check: je kunt het doel hardop noemen zonder "misschien".)
2. **Kies de rol** die de taak het beste uitvoert — specifiek ("senior software engineer die reviewt op security"), niet vleiend ("wereldbeste expert").
3. **Schrijf taak + context + grenzen uit.** Taak als imperatief, context als feiten, grenzen als expliciete verboden (anti-patroon 1, 2, 5). (Check: elke grens staat er letterlijk in.)
4. **Specificeer het outputformaat.** Lengte, structuur, volgorde (bijv. "eerst findings, dan ontbrekende tests, als laatste optionele verbeteringen"), placeholders als `<ONDERWERP>`.
5. **Bouw bewijsverplichtingen in.** "Verifieer tegen de bron", "benoem aannames", "label onzekerheid" (anti-patroon 3).
6. **Test de prompt echt.** Draai hem minimaal 2× tegen het model; check of de output aan stap 1 voldoet en of de grenzen gehouden werden. (Check: 2 runs, vergelijkbaar resultaat, geen grensoverschrijding.)
7. **Sla op met metadata** in de bibliotheek: wanneer/waarvoor/welke agent, bronvermelding, en een status-label (`actief` / `[VEROUDERD]`).

## Examples

**Zwak:** "Maak een mooi dashboard voor mijn verkoopdata."

**Sterk (volgens deze skill):**
```
Je bent een frontend-engineer gespecialiseerd in datavisualisatie.
TAAK: bouw een verkoopdashboard in Streamlit op basis van sales.csv.
CONTEXT: intern tool voor dagelijks gebruik door 3 medewerkers.
GRENZEN: geen externe netwerk-calls; analyseer de data eerst en benoem
aannames vóór je code schrijft; implementeer de kleinste veilige versie.
OUTPUT: eerst een korte data-analyse (max 10 regels), daarna de code.
BENNOEM expliciet aannames over de kolomstructuur.
```

**Diagnose-voorbeeld:** een prompt zonder grenzen leverde in de test (zie Tests) onmiddellijk code mét hardcoded paden op. Na toevoeging van één grens ("geen hardcoded paden, lees pad uit argument") gaf dezelfde prompt pad-parametrische code — meetbaar verschil in 2/2 runs.

**Valkuil:** grenzen die het model kan "vergeten" halverwege lange outputs. Zet de belangrijkste verboden zowel aan het begin als aan het eind van de prompt.

## Tests

Automatisch getest met pytest — **10/10 passed** (bewijs onderaan):
1. Anti-patroon-checker herkent alle 6 familie-anti-patronen in een prompttekst.
2. Anti-patroon-checker geeft géén vals alarm op een schone prompt.
3. Prompt-validatie weigert prompts zonder taak, zonder rol, of zonder outputformaat.
4. Placeholder-check vindt `<ONDERWERP>`-achtige markers en vlagt ongesloten placeholders.
5. De 2-runs-gelijkheid helper vergelijkt outputsets correct.

Zie `test_prompt_engineering.py` (bewijs: `pytest -q` → 10 passed, 0 failed).
Daarnaast: diagnose-claim runtime gevalideerd (`/tmp/diagnose_bewijs.py`, exit 0) —
grenzen in een prompt veranderen de output meetbaar.

## Done

- ✅ Registercheck: geen overlap in het brein (geen bestaande skill "Prompt Engineering"; `prompts/` is bronmateriaal, niet skill).
- ✅ Skill geschreven volgens vast format (Goal / Knowledge / Steps / Examples / Tests / Done).
- ✅ Tests echt uitgevoerd: 10/10 groen (pytest, bewijs in curatievoorstel).
- ✅ Tegenlezen: gedaan aan de hand van de anti-patronen- en meta-prompts-bron.
- ✅ Curatievoorstel geplaatst in `inbox/`.
