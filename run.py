import uvicorn
from bayesian_ab_testing.api import app

if __name__ == "__main__":
    uvicorn.run(app)