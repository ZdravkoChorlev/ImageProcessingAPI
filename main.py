from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello"}

@app.post("/image/")
def add_img():
    return {"message": "Success"}

@app.get("/retrieve")
def retrieve_img():
    return "Success"
