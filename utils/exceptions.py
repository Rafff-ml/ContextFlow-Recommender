from fastapi.responses import JSONResponse

def handle_exception(e):

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server error",
            "message": str(e)
        }
    )