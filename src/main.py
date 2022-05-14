'''

Links:
https://camillovisini.com/article/abstracting-FastAPI-services/
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root():
    '''
    Message for root GET.
    '''
    return {'Message': 'Hello World'}
