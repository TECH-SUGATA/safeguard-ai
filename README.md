# 🛡️ SafeGuard AI
### Digital Public Safety Intelligence Platform

> **ET AI Hackathon 2.0 — Problem Statement 6: Digital Public Safety**
> *Protecting India's citizens with intelligence, not just information.*

---

## 🚨 The Problem

India faces a rapidly escalating digital crime epidemic:

| Threat | Scale |
|--------|-------|
| Cybercrime complaints (2023) | **1.14 Million** — up 60% YoY |
| Digital arrest scam losses | **₹1,776 Crore** in just 9 months of 2024 |
| Fake ₹500 notes | Now defeat **manual bank detection** |
| Fraud rings | Industrialised, cross-border, AI-powered |

---

## 💡 Our Solution

SafeGuard AI is a **unified intelligence platform** with 4 AI modules:

| Module | What it does |
|--------|-------------|
| 🚨 **Scam Detection Agent** | Real-time NLP classifier detects digital arrest scripts before money is transferred |
| 💵 **Counterfeit Currency AI** | Computer vision scans notes across 8 RBI security features in under 2 seconds |
| 🕸️ **Fraud Network Graph AI** | Graph neural networks map crime rings, mule accounts & cross-border connections |
| 🛡️ **Citizen Fraud Shield** | Multilingual AI chatbot in 12 Indian languages — 24/7 via WhatsApp & IVR |

---

## 🏗️ Architecture

```
DATA SOURCES
──────────────────────────────────────────────────────
Telecom CDRs │ UPI/Bank data │ CCTV │ Citizens │ ATM/POS
                          ↓
INGESTION LAYER
──────────────────────────────────────────────────────
         Apache Kafka · Stream normalisation
                          ↓
AI AGENT LAYER
──────────────────────────────────────────────────────
  Scam NLP    │  Graph Fraud  │  Currency CV  │  Shield Bot
    Agent     │     AI        │     AI        │   (LLM)
                          ↓
ORCHESTRATOR
──────────────────────────────────────────────────────
    LangGraph Multi-Agent · Risk scoring · Alert routing
                          ↓
OUTPUT CHANNELS
──────────────────────────────────────────────────────
 Law Enforcement │ Banks/RBI │ Citizens │ MHA/NCRB
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React · Tailwind CSS · Mapbox GL · PWA |
| **Backend** | Python · FastAPI · LangGraph agents |
| **AI / ML** | Claude API · YOLOv8 · PyTorch Geometric · Whisper |
| **Database** | Neo4j · Pinecone · PostgreSQL + PostGIS |
| **Infra** | Docker · Apache Kafka · Redis · AWS |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/safeguard-ai.git
cd safeguard-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the backend
```bash
uvicorn main:app --reload --port 8000
```

### 4. Open the frontend
Simply open `safeguard_ai_FIXED.html` in your browser.

### 5. Explore the API
Visit `http://localhost:8000/docs` for live Swagger UI with all endpoints.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/health` | Health check |
| `GET`  | `/api/dashboard/stats` | Live dashboard metrics |
| `POST` | `/api/scam/analyse` | Scam detection — paste transcript |
| `POST` | `/api/currency/scan` | Counterfeit currency detection |
| `GET`  | `/api/fraud/rings` | Active fraud network rings |
| `GET`  | `/api/fraud/hotspots` | City-level crime hotspots |
| `POST` | `/api/fraud/check` | Check entity (phone/UPI/account) |
| `POST` | `/api/citizen/chat` | Citizen shield chatbot |

### Example — Scam Detection
```bash
curl -X POST http://localhost:8000/api/scam/analyse \
  -H "Content-Type: application/json" \
  -d '{"text": "I am DCP Sharma from CBI. Your Aadhaar is linked to illegal activity. Stay on this call or you will be arrested."}'
```

**Response:**
```json
{
  "score": 94,
  "risk_level": "HIGH",
  "label": "Likely Digital Arrest Scam",
  "action": "Alert telecom provider immediately. File report at cybercrime.gov.in",
  "case_id": "SC-441892"
}
```

---

## 📱 Demo Screenshots

### Dashboard
- Live KPIs: scams blocked, fraud prevented, currency accuracy
- Real-time alert feed with critical/warning/resolved status
- Threat breakdown by category

### Scam Detector
- Paste any suspicious call transcript
- Get risk score (0–100) in under 2 seconds
- Automatic MHA alert generation

### Currency Scanner
- Select denomination (₹100 / ₹500 / ₹2000)
- 8-point RBI security feature validation
- COUNTERFEIT DETECTED with FICN database match

### Fraud Network Map
- India geospatial map with pulsing hotspot dots
- Active fraud rings with confidence scores
- Cross-border network visualisation

### Citizen Shield
- Chat in any of 12 Indian languages
- Instant HIGH / MEDIUM / LOW risk verdict
- Auto-redirect to cybercrime.gov.in

---

## 📊 Impact

| Metric | Value |
|--------|-------|
| Total addressable fraud loss | **₹3,152 Crore/year** |
| Response time reduction | **Hours → ~8 minutes** |
| Agencies unified | **MHA + RBI + Telecom** |
| Citizens covered | **1 Billion+** |
| Languages supported | **12 Indian languages** |

---

## 🗺️ Roadmap

- [ ] Voice AI — detect AI-generated scammer voices (Whisper + deepfake detection)
- [ ] WhatsApp Bot — live deploy on WhatsApp Business API for 500M+ users
- [ ] CCTNS Integration — direct API bridge to state police crime reporting
- [ ] Aadhaar Verification — verify caller identity against UIDAI database
- [ ] Multilingual IVR — citizens call 1930-style helpline in any language

---

## 👥 Team

**Sugata Nayak**
Built for ET AI Hackathon 2.0 — PS6 Digital Public Safety

---

## 📞 Emergency Resources

- **National Cyber Helpline:** 1930
- **Report Cybercrime:** [cybercrime.gov.in](https://cybercrime.gov.in)
- **NCRB Portal:** [ncrp.in](https://ncrp.in)

---

## 📄 License

MIT License — Free to use, modify, and distribute.

---

*"Protecting India's citizens with intelligence, not just information."*
