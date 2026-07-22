from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import re, random, json
from datetime import datetime

app = FastAPI(title="SafeGuard AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────
# MODELS
# ─────────────────────────────────────────
class ScamRequest(BaseModel):
    text: str
    language: Optional[str] = "en"

class CitizenRequest(BaseModel):
    message: str
    language: Optional[str] = "en"

class FraudNetworkRequest(BaseModel):
    account_id: Optional[str] = None
    phone_number: Optional[str] = None
    upi_id: Optional[str] = None

# ─────────────────────────────────────────
# 1. SCAM DETECTION AGENT
# ─────────────────────────────────────────
SCAM_KEYWORDS = {
    "authority": ["cbi", "ed", "customs", "police", "court", "rbi", "income tax", "narcotics", "ib", "interpol", "cbdt"],
    "threat":    ["arrest", "fir", "case", "crime", "warrant", "freeze", "seized", "illegal", "action"],
    "urgency":   ["stay on call", "do not disconnect", "immediately", "within 2 hours", "last chance"],
    "personal":  ["aadhaar", "pan card", "bank account", "otp", "pin", "password", "cvv"],
    "digital_arrest": ["video call", "video verification", "digital arrest", "online fir", "cyber cell"],
    "money":     ["transfer", "send money", "upi", "deposit", "bail amount", "fine", "penalty"],
}

SCAM_PATTERNS = [
    {"name": "Authority impersonation", "weight": 30},
    {"name": "Digital arrest threat",   "weight": 25},
    {"name": "Urgency / isolation",     "weight": 20},
    {"name": "Personal data demand",    "weight": 15},
    {"name": "Financial coercion",      "weight": 10},
]

@app.post("/api/scam/analyse")
async def analyse_scam(req: ScamRequest):
    text = req.text.lower()
    matched = {}
    total_score = 0
    for category, keywords in SCAM_KEYWORDS.items():
        hits = [k for k in keywords if k in text]
        if hits:
            matched[category] = hits
            total_score += len(hits) * 8

    total_score = min(total_score, 97)
    if not matched:
        total_score = max(5, random.randint(5, 18))

    if total_score >= 70:
        risk_level = "HIGH"
        label = "Likely Digital Arrest Scam"
        action = "Alert telecom provider immediately. File report at cybercrime.gov.in"
    elif total_score >= 40:
        risk_level = "MEDIUM"
        label = "Suspicious — verify carefully"
        action = "Do not share personal details. Call 1930 to verify."
    else:
        risk_level = "LOW"
        label = "Appears legitimate"
        action = "Stay cautious. Never share OTP or passwords."

    return {
        "score": total_score,
        "risk_level": risk_level,
        "label": label,
        "action": action,
        "matched_categories": matched,
        "patterns": [p for p in SCAM_PATTERNS if any(k in text for kws in SCAM_KEYWORDS.values() for k in kws)],
        "timestamp": datetime.utcnow().isoformat(),
        "case_id": f"SC-{random.randint(100000,999999)}"
    }

# ─────────────────────────────────────────
# 2. COUNTERFEIT CURRENCY DETECTION
# ─────────────────────────────────────────
SECURITY_CHECKS = [
    {"id": "microprint",   "name": "Microprint thread",      "description": "RBI lettering on security thread"},
    {"id": "hologram",     "name": "Security hologram",      "description": "Colour-shift holographic strip"},
    {"id": "serial",       "name": "Serial number pattern",  "description": "Ascending size + spacing validation"},
    {"id": "uv",           "name": "UV feature analysis",    "description": "Fluorescent ink under UV light"},
    {"id": "ovi",          "name": "Optically variable ink", "description": "Colour shift from green to blue"},
    {"id": "watermark",    "name": "Watermark depth",        "description": "Gandhi portrait watermark clarity"},
    {"id": "intaglio",     "name": "Intaglio printing",      "description": "Raised print tactile feel simulation"},
    {"id": "seethrough",   "name": "See-through register",   "description": "Floral pattern alignment check"},
]

@app.post("/api/currency/scan")
async def scan_currency(denomination: str = "500", note_id: Optional[str] = None):
    checks = []
    fail_count = 0
    for chk in SECURITY_CHECKS:
        # Simulate: genuine notes pass 7-8 checks, counterfeits fail 2-4
        is_genuine_sim = random.random() > 0.15
        if not is_genuine_sim:
            fail_count += 1
        checks.append({
            "id": chk["id"],
            "name": chk["name"],
            "description": chk["description"],
            "status": "PASS" if is_genuine_sim else "FAIL",
            "confidence": round(random.uniform(0.88, 0.99), 2) if is_genuine_sim else round(random.uniform(0.72, 0.89), 2)
        })

    is_counterfeit = fail_count >= 2
    overall_confidence = round(random.uniform(0.94, 0.99), 2) if not is_counterfeit else round(random.uniform(0.87, 0.95), 2)

    return {
        "denomination": denomination,
        "is_counterfeit": is_counterfeit,
        "verdict": "COUNTERFEIT DETECTED" if is_counterfeit else "GENUINE NOTE",
        "overall_confidence": overall_confidence,
        "checks_failed": fail_count,
        "checks_passed": len(SECURITY_CHECKS) - fail_count,
        "security_checks": checks,
        "ficn_db_match": is_counterfeit and random.random() > 0.4,
        "serial_pattern": f"{random.choice(['4BG','8EK','2MN','5ZA'])}{random.randint(100000,999999)}",
        "report_id": f"FICN-{random.randint(10000,99999)}",
        "timestamp": datetime.utcnow().isoformat(),
        "action_required": "Confiscate and report to nearest RBI office" if is_counterfeit else "Note cleared for circulation"
    }

# ─────────────────────────────────────────
# 3. FRAUD NETWORK GRAPH
# ─────────────────────────────────────────
FRAUD_RINGS = [
    {"id":"FRG-2291","name":"Jharkhand Compound Ring","nodes":47,"loss_cr":12.4,"confidence":0.91,"severity":"CRITICAL","state":"Jharkhand","cross_border":True,"country":"Myanmar"},
    {"id":"MUL-0091","name":"Delhi Mule Network","nodes":23,"loss_cr":3.1,"confidence":0.78,"severity":"HIGH","state":"Delhi","cross_border":False,"country":None},
    {"id":"JOB-1142","name":"Rajasthan Job Scam Cluster","nodes":15,"loss_cr":1.8,"confidence":0.65,"severity":"ELEVATED","state":"Rajasthan","cross_border":False,"country":None},
    {"id":"UPI-3344","name":"Mumbai UPI Phishing Ring","nodes":31,"loss_cr":5.2,"confidence":0.84,"severity":"CRITICAL","state":"Maharashtra","cross_border":False,"country":None},
    {"id":"FICN-0812","name":"Northern FICN Distribution","nodes":12,"loss_cr":2.1,"confidence":0.72,"severity":"HIGH","state":"Punjab","cross_border":True,"country":"Pakistan"},
]

HOTSPOTS = [
    {"city":"Delhi NCR","lat":28.6,"lng":77.2,"cases":412,"severity":"CRITICAL"},
    {"city":"Mumbai",   "lat":19.0,"lng":72.8,"cases":287,"severity":"CRITICAL"},
    {"city":"Kolkata",  "lat":22.5,"lng":88.3,"cases":134,"severity":"HIGH"},
    {"city":"Bengaluru","lat":12.9,"lng":77.5,"cases":98, "severity":"ELEVATED"},
    {"city":"Lucknow",  "lat":26.8,"lng":80.9,"cases":88, "severity":"ELEVATED"},
    {"city":"Chennai",  "lat":13.0,"lng":80.2,"cases":76, "severity":"ELEVATED"},
    {"city":"Patna",    "lat":25.6,"lng":85.1,"cases":64, "severity":"HIGH"},
    {"city":"Jaipur",   "lat":26.9,"lng":75.7,"cases":52, "severity":"ELEVATED"},
]

@app.get("/api/fraud/rings")
async def get_fraud_rings():
    return {"rings": FRAUD_RINGS, "total_active": len(FRAUD_RINGS), "timestamp": datetime.utcnow().isoformat()}

@app.get("/api/fraud/hotspots")
async def get_hotspots():
    return {"hotspots": HOTSPOTS, "timestamp": datetime.utcnow().isoformat()}

@app.post("/api/fraud/check")
async def check_fraud_entity(req: FraudNetworkRequest):
    risk = random.choice(["HIGH", "MEDIUM", "LOW"])
    linked_ring = random.choice(FRAUD_RINGS) if risk != "LOW" else None
    return {
        "entity": req.account_id or req.phone_number or req.upi_id,
        "risk_level": risk,
        "linked_ring": linked_ring,
        "victim_count": random.randint(0, 200) if risk != "LOW" else 0,
        "flagged_transactions": random.randint(0, 50) if risk != "LOW" else 0,
        "timestamp": datetime.utcnow().isoformat()
    }

# ─────────────────────────────────────────
# 4. CITIZEN SHIELD CHATBOT
# ─────────────────────────────────────────
RESPONSES = [
    {
        "triggers": ["cbi","ed","customs","arrested","aadhaar","digital arrest","stay on call","video call"],
        "reply": "🚨 DIGITAL ARREST SCAM DETECTED. No government agency (CBI/ED/Customs) will ever ask you to stay on a video call or threaten arrest by phone. Hang up IMMEDIATELY. Do NOT transfer any money. File a complaint at cybercrime.gov.in or call 1930.",
        "risk": "HIGH"
    },
    {
        "triggers": ["otp","bank","account","transfer","send money","upi","pay"],
        "reply": "⚠️ HIGH FRAUD RISK. Never share OTPs, PINs, or passwords with anyone — including people claiming to be from your bank. Legitimate banks NEVER ask for OTP over a call. Call your bank's official helpline immediately.",
        "risk": "HIGH"
    },
    {
        "triggers": ["job","offer","work from home","fees","registration","deposit"],
        "reply": "⚠️ JOB SCAM ALERT. Genuine employers never ask for fees, registration charges, or deposits to secure a job. This matches known job scam patterns. Do NOT pay anything. Report at ncrp.in.",
        "risk": "HIGH"
    },
    {
        "triggers": ["lottery","won","prize","claim","congratulations"],
        "reply": "🚨 LOTTERY SCAM. You cannot win a lottery you did not enter. This is a classic advance-fee fraud. Block the contact immediately and report to cybercrime.gov.in.",
        "risk": "HIGH"
    },
    {
        "triggers": ["fake note","currency","counterfeit","rupee","note"],
        "reply": "If you have received a suspicious currency note, do NOT try to pass it on. Take it to your nearest bank branch or police station. Counterfeit notes can be reported to the RBI or local police.",
        "risk": "MEDIUM"
    },
    {
        "triggers": ["safe","genuine","real","verify","check","confirm","legitimate"],
        "reply": "To verify if something is genuine: (1) Never share personal info without verification (2) Call the official helpline of the organisation directly (3) Check cybercrime.gov.in for known scam alerts. Stay safe!",
        "risk": "LOW"
    },
]

DEFAULT_REPLY = "I've noted your concern. If you feel unsafe or believe you are being scammed, please call the National Cyber Helpline immediately: 1930. You can also report online at cybercrime.gov.in. Your safety is the priority."

@app.post("/api/citizen/chat")
async def citizen_chat(req: CitizenRequest):
    text = req.message.lower()
    matched = next((r for r in RESPONSES if any(t in text for t in r["triggers"])), None)
    reply = matched["reply"] if matched else DEFAULT_REPLY
    risk = matched["risk"] if matched else "LOW"
    return {
        "reply": reply,
        "risk_level": risk,
        "helpline": "1930",
        "report_url": "https://cybercrime.gov.in",
        "case_ref": f"CZ-{random.randint(100000,999999)}",
        "timestamp": datetime.utcnow().isoformat()
    }

# ─────────────────────────────────────────
# 5. DASHBOARD STATS
# ─────────────────────────────────────────
@app.get("/api/dashboard/stats")
async def get_stats():
    return {
        "scams_blocked_today": random.randint(1200, 1300),
        "fraud_prevented_cr": round(random.uniform(4.0, 4.5), 1),
        "currency_accuracy_pct": round(random.uniform(97.8, 99.1), 1),
        "active_networks": random.randint(12, 16),
        "alerts": [
            {"type":"CRITICAL","text":"Digital arrest scam — active session detected","time":"2m ago"},
            {"type":"CRITICAL","text":"FICN cluster — SBI ATM network, Patna zone","time":"8m ago"},
            {"type":"WARNING", "text":"Fraud ring expansion — 7 new mule accounts","time":"31m ago"},
            {"type":"RESOLVED","text":"Citizen report verified and resolved","time":"1h ago"},
        ],
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "SafeGuard AI API", "version": "1.0.0"}
