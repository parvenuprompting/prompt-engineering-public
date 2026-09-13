"""Tests voor Skill: Prompt Engineering — gevalideerd door Skilly Bang, 10 sept 2026."""
import re
import pytest

# --- Referentie-implementatie (de skill als code) ---

ANTI_PATRONEN = {
    "actie-voor-analyse": r"geen code voordat de analyse",
    "read-only-zonder-uitzondering": r"read-only modus",
    "claims-zonder-label": r"niet geverifieerd",
    "visuele-ruis": r"geen trendeffect",
    "scope-schending": r"kleinste veilige wijziging",
    "hype-in-taal": r"\brevolutionair\b",
}

def check_anti_patronen(prompt: str) -> set:
    """Geeft de set anti-patronen die in de prompt (positief) voorkomen."""
    low = prompt.lower()
    return {naam for naam, pat in ANTI_PATRONEN.items() if re.search(pat, low)}

VERPLICHT = ["rol", "taak", "output"]

def valideer_prompt(prompt: str) -> list:
    """Geeft lijst van ontbrekende verplichte onderdelen (leeg = geldig)."""
    low = prompt.lower()
    ontbreek = []
    for v in VERPLICHT:
        if v == "rol" and not re.search(r"je bent een", low):
            ontbreek.append("rol")
        if v == "taak" and not re.search(r"\btaak:", low):
            ontbreek.append("taak")
        if v == "output" and not re.search(r"\boutput:", low):
            ontbreek.append("output")
    return ontbreek

def check_placeholders(prompt: str) -> list:
    """Vindt ongesloten placeholders zoals <ONDERWERP zonder >."""
    return re.findall(r"<[A-Z_]+(?=[^>]*$)", prompt, re.M)

def runs_gelijk(a: list, b: list, tol: float = 0.0) -> bool:
    """Vergelijk 2 prompt-runs (lijsten van resultaat-strings) op gelijkheid."""
    if len(a) != len(b):
        return False
    verschillen = 0
    for x, y in zip(a, b):
        if x.strip().lower() != y.strip().lower():
            verschillen += 1
    return verschillen <= tol

# --- Tests 1+2: anti-patroon-detectie ---

def test_alle_zes_anti_patronen_herkend():
    prompt = (
        "Schrijf geen code voordat de analyse is afgerond. READ-ONLY MODUS. "
        "Label statistische claims als niet geverifieerd. Geen trendeffect. "
        "Implementeer de kleinste veilige wijziging. Dit is niet revolutionair."
    )
    assert check_anti_patronen(prompt) == set(ANTI_PATRONEN)

def test_geen_vals_alarm_op_schone_prompt():
    prompt = (
        "Je bent een data-analist. Taak: tel rijen in sales.csv. "
        "Output: een getal en de gebruikte query."
    )
    assert check_anti_patronen(prompt) == set()

# --- Tests 3: validatie weigert incompleet ---

def test_weigert_zonder_taak_en_output():
    p = "Je bent een senior engineer. Doe iets nuttigs."
    assert set(valideer_prompt(p)) == {"taak", "output"}

def test_weigert_zonder_rol():
    p = "Taak: schrijf rapport. Output: markdown, max 20 regels."
    assert valideer_prompt(p) == ["rol"]

def test_accepteert_compleet():
    p = ("Je bent een reviewer. Taak: review diff. Grenzen: read-only modus. "
         "Output: findings eerst, daarna ontbrekende tests.")
    assert valideer_prompt(p) == []

# --- Tests 4: placeholders ---

def test_placeholder_gesloten_gevonden():
    assert check_placeholders("Ontwerp een API voor <BESCHRIJVING>.") == []

def test_placeholder_ongesloten_gevlagd():
    assert check_placeholders("Ontwerp een API voor <BESCHRIJVING zonder afsluiting") == ["<BESCHRIJVING"]

# --- Tests 5: 2-runs-gelijkheid ---

def test_runs_gelijk_normaal():
    assert runs_gelijk(["Ok"], ["ok "]) is True

def test_runs_ongelijk():
    assert runs_gelijk(["Ok", "Anders"], ["ok", "nieuw"]) is False

def test_runs_len_verschil():
    assert runs_gelijk(["Ok"], ["ok", "extra"]) is False
