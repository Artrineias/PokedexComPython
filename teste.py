from fastapi import FastAPI
import main
main = FastAPI()

@main.get("/")
def roda():
    return main.inicial()
