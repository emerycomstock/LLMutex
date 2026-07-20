from fastapi import FastAPI 
from api.routers import inference

# Define FastAPI server
app = FastAPI()
app.include_routers(inference.router)

def main():
    print("Hello from llmutex!")
    # TODO: Use uvicorn to run the server and listen for requests

if __name__ == "__main__":
    main()
