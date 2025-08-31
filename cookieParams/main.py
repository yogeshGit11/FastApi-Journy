from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()


@app.get("/showproducts")
async def show_products(session_id: Annotated[str | None, Cookie()] = None):
    if session_id:
        return {
            "Msg": f"Your Prefernace product. session id:{session_id}",
            "products": ["HRX brands", "SONY LED"],
        }
    else:
        return {
            "MSg": "NO Seesion ID Showing default products",
            "products": ["SamsungTV", "NOKIA"],
        }
