from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/passphrase")
async def index(limit=10, encrypted : bool = True, sort: Optional[str] = None):
    if encrypted:
        return {"data": f'{limit} encrypted passphrases from the database'}
    else:
        return {"data": f'{limit} passphrases from the database'}

@app.get('/passphrase/unused')
async def unused():
    return {'data':'aall unused passphrase'}

@app.get('/passphrase/{id}')
async def show(id:int):
    return {'data' : id}


@app.get('/passphrase/{id}/user')
async def show(id, limit=10):
    return {'data' : {'1', '2'}}