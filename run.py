import uvicorn
from AB_Testing.api import app

if __name__ == "__main__":
    uvicorn.run(app)