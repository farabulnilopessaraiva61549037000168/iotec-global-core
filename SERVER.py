import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from fastapi import FastAPI

from pydantic import BaseModel



app = FastAPI()



class Order(BaseModel):
    pass



    cliente:str

    pais:str

    setor:str

    produto:str

    valor:float



@app.get("/")



def home():
    pass



    return {

        "status":"online"

    }



@app.get("/api/orders")



def get_orders():
    pass



    return []



@app.post("/api/orders")



def create_order(order:Order):
    pass



    return {



        "success":True,

        "cliente":order.cliente



    }






