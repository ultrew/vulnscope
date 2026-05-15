# VulnScope

VulnScope is a Python-based cybersecurity CLI tool that aggregates public bug bounty and vulnerability disclosure programs from multiple platforms.

The project focuses on:
- public program discovery
- target aggregation
- operator filtering
- JSON export workflows
- modular source ingestion

Current supported platforms:
- YesWeHack
- Bugcrowd

Future planned integrations:
- HackerOne
- Intigriti
- custom recon enrichment

---

# Features

- Multi-source bug bounty aggregation
- Unified normalized program schema
- CLI filtering
- Difficulty classification
- JSON export support
- Rich terminal table output
- Modular architecture
- Extensible source system

---

# Screenshots To Add

Create a folder:

```text
screenshots/
```

Add these screenshots:

## 1. Main Program Output

Filename:

```text
screenshots/main-output.png
```

Take screenshot of:

```bash
python main.py
```

Include:
- table output
- program count
- platforms

---

## 2. Platform Filtering

Filename:

```text
screenshots/platform-filter.png
```

Take screenshot of:

```bash
python main.py --platform yeswehack
```

---

## 3. Difficulty Filtering

Filename:

```text
screenshots/difficulty-filter.png
```

Take screenshot of:

```bash
python main.py --difficulty beginner
```

---

## 4. JSON Export

Filename:

```text
screenshots/export-output.png
```

Take screenshot of:

```bash
python main.py --export
```

Also show:

```bash
cat results.json
```

---

# Project Structure

```text
vulnscope/
├── cli/
│   ├── __init__.py
│   └── commands.py
│
├── core/
│   ├── __init__.py
│   ├── classifier.py
│   ├── scraper.py
│   └── scoring.py
│
├── output/
│   ├── __init__.py
│   └── json_export.py
│
├── sources/
│   ├── __init__.py
│   ├── bugcrowd.py
│   ├── hackerone.py
│   └── yeswehack.py
│
├── screenshots/
├── main.py
├── results.json
└── README.md
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/vulnscope.git
```

Move into project:

```bash
cd vulnscope
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate virtual environment:

Linux:

```bash
source myenv/bin/activate
```

Windows:

```powershell
myenv\Scripts\activate
```

Install dependencies:

```bash
pip install typer rich requests beautifulsoup4
```

---

# Usage

## Run All Sources

```bash
python main.py
```

---

## Filter By Platform

```bash
python main.py --platform yeswehack
```

```bash
python main.py --platform bugcrowd
```

---

## Filter By Difficulty

```bash
python main.py --difficulty beginner
```

---

## Export Results

```bash
python main.py --export
```

Generated file:

```text
results.json
```

---

# Example JSON Schema

```json
{
    "name": "Example Program",
    "platform": "YesWeHack",
    "url": "https://yeswehack.com/programs/example",
    "scope": "example-scope",
    "mobile": false,
    "graphql": false,
    "waf": false,
    "severity": "unknown"
}
```

---

# Architecture

## Source Layer

Responsible for:
- fetching platform data
- extracting program information
- normalizing records

Files:

```text
sources/
```

---

## Core Layer

Responsible for:
- aggregation
- deduplication
- classification
- scoring

Files:

```text
core/
```

---

## CLI Layer

Responsible for:
- user interaction
- filtering
- rendering
- operator workflow

Files:

```text
cli/
```

---

## Output Layer

Responsible for:
- JSON exports
- automation compatibility
- downstream tooling support

Files:

```text
output/
```

---

# Current Limitations

- HackerOne scraping currently unstable due to anti-bot protections
- Difficulty scoring system is still basic
- No async ingestion yet
- No recon enrichment yet
- No live scope validation yet

---

# Future Roadmap

Planned improvements:

- Improved Bugcrowd extraction
- Stable HackerOne ingestion
- Intigriti integration
- Scope enrichment
- Wildcard detection
- GraphQL detection
- Live target validation
- Async fetching
- CSV export
- Recon integrations
- Subdomain enrichment

---

# Resume Description

Developed VulnScope, a modular Python CLI tool for aggregating and filtering public bug bounty programs across multiple platforms. Implemented modular source ingestion, structured normalization, JSON export functionality, and operator-focused filtering workflows.

---

# License

MIT License

