# AI Password Strength Auditor & Risk Scorer

An intelligent, zero-knowledge password security auditing platform. This system evaluates passwords along structural, probabilistic, and empirical threat-intelligence vectors without ever storing, logging, or transmitting raw credentials over a network.

By shifting the paradigm from rigid, legacy compliance checkboxes (e.g., *"must contain 1 capital letter and 1 symbol"*) to dynamic risk scoring, this tool mirrors how modern enterprise security teams assess credential hygiene and breach vulnerability.

---

## 🎯 Overview

Traditional password validation methods are fundamentally broken. Attackers do not guess passwords using random character combinations — they leverage massive credential leaks, dictionary permutations, and optimized pattern generators.

This platform evaluates sub-string entropy, repetition behaviors, dictionary matches, and cryptographic breach frequencies to output a granular risk profile scaling from `0.0` (Low Risk) to `1.0` (Critical Risk).

---

## 🔒 Threat Model & Security Guarantees

- **Zero-Knowledge Ephemeral Design:** Passwords are processed strictly within isolated, transient memory frames. They are never committed to persistent storage, cache layers, databases, or application log files.
- **Log Scrubbing:** Application layers explicitly omit raw payload data from standard output, preventing structural leaks through downstream log collectors.
- **Local Cryptographic Lookup:** To verify breach exposure, raw inputs are instantly transformed into SHA-256 hexadecimal digests. Evaluation happens entirely offline against pre-computed local data, ensuring no cleartext data ever traverses the wire.

---

## 📁 Project Structure

```
password-risk-scorer/
├── data/
│   ├── processed/          # Compiled, safe cryptographic breach records
│   └── raw/                # Source intelligence files
├── src/
│   ├── api/                # FastAPI application layer
│   ├── data/               # Threat data ingestion & hash engines
│   ├── features/           # Algorithmic metric and entropy extractors
│   ├── scoring/            # Multi-dimensional risk calculation logic
│   └── utils/              # Secure terminal CLI wrappers
├── tests/                  # Integrity verification unit tests
├── .gitignore              # Environment isolation definitions
├── README.md               # Repository documentation
└── requirements.txt        # Pinned Python package map
```

---

## ⚙️ Setup & Installation

Follow these steps to isolate dependencies and prepare the system database locally.

### 1. Environment Preparation

Clone the repository and spin up an isolated Python virtual environment:

```bash
git clone https://github.com/KingLinux24/password-risk-scorer.git
cd password-risk-scorer
python3 -m venv .venv
```

Activate the environment based on your operating system:

**Linux / macOS (Kali Linux):**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

### 2. Dependency Resolution

Upgrade the core package manager and install production libraries:

```bash
pip install -U pip
pip install -r requirements.txt
```

### 3. Initialize Threat Data

Generate the internal, secure pre-hashed dataset used for breach lookups:

```bash
python src/data/load_breach_stats.py
```

---

## 🚀 How to Run

The engine exposes two distinct execution interfaces designed for security operations and development workflows.

### 1. Command Line Interface (CLI)

Run the standalone script to perform instantaneous, interactive credential audits. The password input field remains hidden as you type to prevent shoulder surfing.

```bash
python -m src.utils.cli
```

**Terminal Interactivity Example:**

```
Enter password (input hidden): 
{
  'risk_score': 0.4, 
  'risk_level': 'medium', 
  'reasons': [
    'Password is shorter than recommended length', 
    'Repeated character patterns detected'
  ]
}
```
<img width="1745" height="155" alt="Screenshot 2026-06-03 095102" src="https://github.com/user-attachments/assets/3a6663c3-fe2d-43ec-8179-523c1f3906e7" />

 
### 2. REST API Engine

Launch the web deployment layer powered by FastAPI and Uvicorn:

```bash
uvicorn src.api.app:app --reload --port 8000
```

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the Swagger/OpenAPI interface.

**Inbound REST Request:**

```json
POST http://127.0.0.1:8000/score
{
  "password": "Ha24@#$#miler7345"
}
```

**Outbound HTTP Response (200 OK):**

```json
{
  "risk_score": 0.0,
  "risk_level": "low",
  "reasons": []
}
```
<img width="1830" height="712" alt="Screenshot 2026-06-03 094847" src="https://github.com/user-attachments/assets/4c169dd0-a97b-4d66-9dcd-ff8660e73586" />

---

## 🧠 Scoring Methodology

The final compound risk profile aggregates specific mathematical penalties up to a logical limit of `1.0`:

| Analysis Vector | Risk Weight | Evaluation Criteria |
|---|---|---|
| Length Boundary | +0.25 | Overall text string spans fewer than 12 total characters. |
| Character Diversity | +0.20 | String references fewer than 3 separate character groups (lowercase, uppercase, digits, symbols). |
| Dictionary Token Match | +0.20 | Contains common contextual, administrative, or system default phrases. |
| Structural Repetition | +0.15 | Employs sequential back-to-back repeating characters (e.g., `aaa`, `111`). |
| Prior Breach Exposure | +0.40 | SHA-256 footprint is found within known threat datasets. |

---

## 📈 Enterprise Integration Ideas

- **IAM Registration Gatekeeper:** Embed the REST endpoint directly into your authentication gateway to drop registration requests if the computed payload yields a `risk_score > 0.50`.
- **Corporate Directory Audits:** Run scheduled batch tasks checking corporate Active Directory hashes against this engine to flag vulnerable administrative accounts without compromising core user credentials.
- **Proactive Security UI Elements:** Replace frustrating frontend character requirement lists with an intuitive, dynamic risk meter component driven by the JSON metadata payload.

---

## ⚠️ Limitations & Ethical Notes

- **Static Lookup Bounds:** The basic deployment includes a sample snapshot of historically compromised passwords. For live infrastructure, swap the local text store with an external indexed database or integrate a real-time K-Anonymity lookup interface.
- **Context Blindness:** This standalone library scores passwords as isolated strings. It does not natively correlate user-specific variables such as individual usernames, company tags, or email sub-strings. External orchestration filters should handle context validation.
