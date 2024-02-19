from fastapi import FastAPI, Request, HTTPException , status

import uuid

app = FastAPI()

tanks = []

@app.get("/tank")
def get_tank():
    return tanks

@app.get("/tank/{id}")
async def get_tank_id(id:str):

    for i in tanks:
       if i["id"] == id:
          return{"Tank" : i}
       raise HTTPException(status_code = 404, detail = "Tank was not found")
    
@app.post("/tank",status_code = status.HTTP_201_CREATED)
async def post_tank(request:Request):
   tank = await request.json()
   

   new_uuid = uuid.uuid4()

   tank = {"id":str(new_uuid),**tank}

   tanks.append(tank)
   return(tank)

@app.patch("/tank/{id}", status_code = status.HTTP_200_OK)
async def patch_tank(id: str, request:Request):
   patched_tank = await request.json()

   for i, tank in enumerate(tanks):
      if tank["id"] == id:
         tanks[i] = {**tank,**patched_tank}
         return tank[i]
      raise HTTPException(status_code = 404, detail = "Tank was not Found")
   


@app.delete("/tank{id}", status_code = status.HTTP_200_OK)
def delete_tank(id:str):
   for i in range(len(tanks)):
      if tanks[i]["id"] == id:
         del tanks[i]
         return()
      raise HTTPException(status_code = 404, detail = "Tank was not found")
