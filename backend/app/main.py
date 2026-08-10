from fastapi import FastAPI

app = FastAPI(
    title="AegisGrid X",
    description="AI-Powered Zero-Trust Cyber Range & Enterprise Security Fabric",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "aegisgrid-x",
    }
