import sys
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

# Fix Windows ProactorEventLoop reset crash (WinError 10054)
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="Cyber Kavach AI Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paste your real Gemini API key below (starts with AIzaSy...)
GEMINI_API_KEY = "AIzaSyB59BYwVvAjnwuL6JkOijjP6nL3fp2PndQ." 
client = genai.Client(api_key=GEMINI_API_KEY)

class ThreatRequest(BaseModel):
    message: str

@app.post("/analyze-threat")
def analyze_threat(payload: ThreatRequest):
    try:
        prompt = f"""
        You are the Cyber Kavach Emergency AI Incident Solver.
        The user has reported the following incident:
        "{payload.message}"

        Analyze the incident and provide a clear, step-by-step resolution:
        🚨 THREAT ASSESSMENT: [CRITICAL / HIGH RISK / SUSPICIOUS / SAFE]
        🔍 CRIME MECHANISM: [How this scam operates in 1-2 concise sentences]
        🛡️ STEP-BY-STEP SOLUTION FOR USER:
        1. [Immediate action: e.g. Do not enter PIN / Block sender / Disconnect call]
        2. [Remediation action: e.g. Freeze account / Report on cybercrime.gov.in / Call 1930]
        3. [Evidence preservation: e.g. Take screenshot of transaction ID / Save chat logs]
        """
        
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return {"status": "success", "analysis": response.text}
    except Exception as e:
        return {"status": "error", "analysis": f"AI Engine Error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)