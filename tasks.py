from robocorp.tasks import task
from robocorp import browser
from pathlib import Path
from urllib.parse import urljoin
import csv
import re
import unicodedata

OUT = Path("saidaDados"); OUT.mkdir(exist_ok=True)
CSV_FILE = OUT / "licitacao-londrina.csv"
RE_MOEDA = re.compile(r"R\$\s*[\d\.\,]+", re.I)

def norm_text(s: str | None) -> str:
    """Normaliza texto: remove NBSP, quebra de linha, múltiplos espaços e 'Ver Mais' sobrando."""
    if not s:
        return ""
    s = s.replace("\xa0", " ")            # NBSP
    s = s.replace("\u200b", "")           # zero width
    s = s.replace("…", "...")             # reticências
    s = s.replace("Ver Mais", "")         # lixeira do portal
    s = " ".join(s.split())               # colapsa espaços/linhas
    # normaliza acentuação (garante composição padrão)
    return unicodedata.normalize("NFC", s)

def clean_money(s: str) -> str:
    """Mantém formato BR no CSV; se vier dentro de um texto maior, extrai a moeda."""
    s = norm_text(s)
    m = RE_MOEDA.search(s)
    return m.group(0) if m else s

def accept_cookies(page):
    for sel in [
        'button:has-text("Aceitar")',
        'button:has-text("Concordo")',
        'button:has-text("OK")',
        '[data-testid="cookie-accept-all"]',
    ]:
        try:
            btn = page.locator(sel).first
            if btn.count() and btn.is_visible():
                btn.click()
                page.wait_for_timeout(250)
                break
        except:
            pass

@task
def fluxo_completo(headless: bool = False):
    """Abre o navegador e acessa a página de licitações de Londrina."""
    url = "https://portal.londrina.pr.gov.br/index.php/licitacao-inicio"
    browser.configure(browser_engine="chromium", headless=headless)
    page = browser.page()
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(2000) 
    accept_cookies(page)
    botao_id = "#sppb-addon-1669140503596"  
    page.click(botao_id)
    page.wait_for_timeout(2000)
