# AkaAPI

### Beskrivelse

AkaAPI er et verktøy for å hente ut informasjon om Akademiet privatskolene. Det inneholder informasjon om elever, ansatte, skoler og generell info om Akademiet.

Programmet er skrevet hovedsakelig i Python med bruk av Flask. Andre språk som er brukt er HTML, CSS og JavaScript.

---

### Oppsett

```zsh
python3 -m venv .venv # Lager virtuelt miljø

source .venv/bin/activate # Aktiverer VEnv

pip install flask # Installerer flask pakken

```

Enkel one-liner kommando:

```zsh
python3 -m venv .venv && source .venv/bin/activate && pip install flask
```

---

<br>

<b>Hvorfor ikke innkludere venv på GitHub? </b> <br>
Jeg valgte å ikke innkludere venv-et på GitHub siden det er en meget stor mappe som lett kan genereres på nytt med å kjøre et par kommandoer. For å ignorere mappen la jeg til en ".gitignore" fil med ".venv" for å ignorere mappen ".venv"

---

### Bruk

For å starte Flask serveren må du være i riktig directory i terminalen først. Kontroller gjerne med ls for å se at riktige filer vises. Så skal <code>python3 app.py</code> kjøres. Da vil adressen bli printet ut og du kan besøke siden.

**!! HUSK !!** <br>
Om programmet kjøres på egen datamaskin vil det være utilgjengelig fra eksterne systemer. Om du ønsker at andre skal besøke siden må den hostes på en annen måte.

---

### Bruk av KI verktøy

I prosjektet brukte jeg KI verktøy på følgende måter:

<ol>
<li>Generere fiktiv data for API'en i <code>data.json</code> fil.

PROMPT: <br> <code>Generer en utfyllende versjon av denne json filen uten ekte informasjon og med felt for lærere, elever på hver skole, linja eleven går på og tilgjengelige linjer. også legg inn relevant nformasjon for hver skole. Dataen skal være for Akademiet VGS så inkluder relevant informasjon som ikke deler PII.</code></li>

<li>Gi enkelte kommandoer i CSS som:<br><code>How to apply pseudo-element CSS</code></li>

<li>Forklare hvordan man kan bruke recursion i jinja2<br><code>how can i make a loop to recursively look through all child nodes and check if any values contain a list to then loop over that?</code></li>
<li>Forklare hvordan man sjekker datatypen til en verdi<br><code>in jinja2, how can i check if a value is a dictionary or array?</code></li>
</ol>
