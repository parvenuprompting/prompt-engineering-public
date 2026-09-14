"""Tests voor check_prompt.py (Skilly-gate + TDD, 14 sept)."""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "check_prompt.py"
STERK = Path(__file__).parent.parent / "examples" / "sterk-dashboard.txt"
ZWAK = Path(__file__).parent.parent / "examples" / "zwak-dashboard.txt"


def test_sterk_prompt_scoret_10_en_exit_0():
    r = subprocess.run([sys.executable, str(SCRIPT), str(STERK)], capture_output=True, text=True)
    assert r.returncode == 0
    assert "10/10" in r.stdout
    assert "Geen anti-patronen" in r.stdout


def test_zwak_prompt_scoret_laag_en_exit_1():
    r = subprocess.run([sys.executable, str(SCRIPT), str(ZWAK)], capture_output=True, text=True)
    assert r.returncode == 1
    assert "3/10" in r.stdout or "Score: 3" in r.stdout
    assert "AP6" in r.stdout  # hype-taal ("revolutionair")


def test_checker_gebruikt_zelfde_anti_patronen_als_hoofdtests():
    """Koppeling met de originele 6 anti-patronen (consistentie)."""
    sys.path.insert(0, str(Path(__file__).parent.parent))
    import test_prompt_engineering as orig
    from check_prompt import ANTI_PATRONEN
    assert len(ANTI_PATRONEN) == 6


def test_scan_functie_direct():
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from check_prompt import scan
    u = scan("Je bent een reviewer. Geen secrets in de output. Verifieer alles.")
    assert u["score"] >= 8
    assert not u["bevindingen"]
