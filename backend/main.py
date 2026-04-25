from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cybersecurity Learning API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOCK_DASHBOARD = {
    "user": {
        "id": "123",
        "name": "João Batista",
        "tryhackmeUsername": "joao_thm",
        "htbStudentId": "HTB-00123"
    },
    "summary": {
        "overallProgress": 0.46,
        "xp": 2450,
        "badges": [
            {"id": "first-10-labs", "name": "Primeiros 10 labs"},
            {"id": "crypto-50", "name": "50% em Criptografia"}
        ]
    },
    "tracks": [
        {"id": "fundamentals", "name": "Fundamentos", "progress": 0.65},
        {"id": "offensive", "name": "Red Team / Pentest", "progress": 0.52},
        {"id": "defensive", "name": "Blue Team / Defesa", "progress": 0.38},
        {"id": "governance", "name": "Governança / CIS", "progress": 0.41}
    ],
    "frameworkCoverage": [
        {
            "frameworkId": "cis-v8.1",
            "frameworkName": "CIS Controls v8.1",
            "implementationGroup": "IG1",
            "controlsTotal": 18,
            "controlsCovered": 11,
            "coverage": 0.61
        }
    ],
    "topSkills": [
        {"skillId": "linux-fundamentals", "name": "Fundamentos de Linux", "progress": 0.9},
        {"skillId": "web-appsec", "name": "Web Application Security", "progress": 0.7}
    ],
    "recommendedChallenges": [
        {
            "challengeId": "thm-cryptographybasics",
            "platform": "TryHackMe",
            "name": "Cryptography Basics",
            "skillId": "crypto-aplicada",
            "reason": "Próximo passo em Criptografia",
            "difficulty": "Easy"
        },
        {
            "challengeId": "htb-web-attacks",
            "platform": "HTB Academy",
            "name": "Web Attacks",
            "skillId": "web-pentest",
            "reason": "Reforçar OWASP Top 10",
            "difficulty": "Medium"
        }
    ]
}

MOCK_SKILLS = [
    {
        "skillId": "net-fundamentals",
        "code": "net-fundamentals",
        "name": "Fundamentos de redes",
        "category": "fundamentals",
        "level": 1,
        "progress": 0.8,
        "frameworks": [
            {"code": "CIS-4", "name": "Secure Configuration of Enterprise Assets"}
        ],
        "challenges": [
            {
                "challengeId": "thm-whatisnetworking",
                "platform": "TryHackMe",
                "slug": "whatisnetworking",
                "name": "What is Networking?",
                "difficulty": "Easy",
                "status": "completed"
            },
            {
                "challengeId": "thm-introtolan",
                "platform": "TryHackMe",
                "slug": "introtolan",
                "name": "Intro to LAN",
                "difficulty": "Easy",
                "status": "in_progress"
            }
        ]
    },
    {
        "skillId": "crypto-aplicada",
        "code": "crypto-aplicada",
        "name": "Criptografia aplicada",
        "category": "fundamentals",
        "level": 2,
        "progress": 0.4,
        "frameworks": [
            {"code": "CIS-3", "name": "Data Protection"}
        ],
        "challenges": [
            {
                "challengeId": "thm-cryptographybasics",
                "platform": "TryHackMe",
                "slug": "cryptographybasics",
                "name": "Cryptography Basics",
                "difficulty": "Easy",
                "status": "in_progress"
            }
        ]
    }
]

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/hello")
def hello():
    return {"message": "Olá, Render! Seu backend FastAPI está no ar."}

@app.get("/api/dashboard/{user_id}")
def get_dashboard(user_id: str):
    data = MOCK_DASHBOARD.copy()
    data["user"] = {**MOCK_DASHBOARD["user"], "id": user_id}
    return data

@app.get("/api/users/{user_id}/skills")
def get_user_skills(user_id: str, level: int | None = None, category: str | None = None):
    skills = MOCK_SKILLS

    if level is not None:
        skills = [s for s in skills if s["level"] == level]

    if category:
        skills = [s for s in skills if s["category"] == category]

    return skills
