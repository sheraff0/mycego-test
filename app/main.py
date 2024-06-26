from io import BytesIO

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from services.common import load_and_convert

app = FastAPI(title="mycego-test")


@app.get("/convert/ya-disk", response_class=StreamingResponse)
def convert(
    link: str
):
    res = load_and_convert(link)

    if not res:
        raise HTTPException(400, "Cannot process images!")

    return StreamingResponse(res, media_type="image/tiff", headers={
        "Content-Disposition": "attachment; filename=Result.tif"
    })
