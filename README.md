# 🤖 RPA - Coleta de Licitações da Prefeitura de Londrina

Junto ao meu amigo <a href="https://github.com/MarceloLuan">Marcelo Luan</a>, este projeto utiliza Robocorp (RPA em Python) para acessar o site da Prefeitura de Londrina, navegar até a seção de licitações públicas e extrair os dados relevantes em um arquivo CSV.

---

## 📌 Funcionalidades
- Acessa automaticamente o [Portal de Licitações de Londrina](https://portal.londrina.pr.gov.br/index.php/licitacao-inicio).
- Aceita cookies de forma automática (quando exibido).
- Clica em botões de navegação (por ID) para acessar os resultados.
- Extrai informações como:
  - Número da licitação  
  - Objeto (descrição)  
  - Modalidade  
  - Data de abertura  
  - Link para detalhes  
- Salva os dados em **CSV** dentro da pasta `saidaDados/`.

---

## 🛠️ Tecnologias utilizadas
- [Robocorp](https://robocorp.com/)  
- [Python 3.10+](https://www.python.org/)  
- Playwright (via `robocorp.browser`)  
- Regex e normalização de textos (`re`, `unicodedata`)  

---
