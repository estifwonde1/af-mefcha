from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app= FastAPI(title="standalone fastapi",version="1.0.0")

@app.get("/health",tags=["Health"])
def health_check():
    return{"status":"ok"}
def main():
    print("Hello from af-meftcha!")


if __name__ == "__main__":
    main()
