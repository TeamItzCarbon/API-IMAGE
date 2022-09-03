from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my-endpoint")
def example_function():
    """
    Documentation for My Api. Soon Add 

    1) This Online Image Works:

    ![This image works](https://telegra.ph/file/fdcd5bfa701a440a590e8.jpg)

    """
    return {"This is My Test Api"}

@app.get("/img/Anime1.png")
async def read_image():
    return FileResponse("example-photo.jpg")
