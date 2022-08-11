from fastapi import FastAPI, HTTPException
from mongita import MongitaClientDisk
from pydantic import BaseModel


class Shape(BaseModel):
    name: str
    no_of_sides: int
    id: int


# shapes = [
#     {"item_name": "Circle", "no_of_sides": 1, "id": 1},
#     {"item_name": "Square", "no_of_sides": 4, "id": 2},
#     {"item_name": "Triangle", "no_of_sides": 3, "id": 3},
# ]

app = FastAPI()  # create an instance of FastAPI class
client = MongitaClientDisk()  # create an instance of MongitaClientDisk class
db = client.db  # create an instance of MongitaClientDisk class
shapes = db.shapes  # collection name is shapes


@app.get("/")  # decorator to map the endpoint to the function
async def root():  # function to return the response
    return {"message": "Hello World"}


# uvicorn main:app --host "0.0.0.0" --port 8000 --reload

@app.get("/shapes")  # decorator to map the endpoint to the function
async def get_shapes():  # function to return the response
    existing_shapes = shapes.find({})  # find all the shapes in the collection
    return [
        {key: shape[key] for key in shape if key != "_id"}
        for shape in existing_shapes
    ]


@app.get("/shapes/{shape_id}")  # decorator to map the endpoint to the function
async def get_shapes_by_id(shape_id: int):  # function to return the response
    # for shape in shapes:
    #     if shape['id'] == shape_id:
    #         return shape
    if shapes.count_documents({"id": shape_id}) > 0:
        shape = shapes.find_one({"id": shape_id})
        return {key: shape[key] for key in shape if key != "_id"}

    raise HTTPException(status_code=404, detail=f"No Shape with {shape_id} found")


@app.post("/shapes")  # decorator to map the endpoint to the function
async def post_shape(shape: Shape):  # function to return the response
    shapes.insert_one(shape.dict())
    return shape


@app.put("/shapes/{shape_id}")  # decorator to map the endpoint to the function
async def update_shape(shape_id: int, shape: Shape):  # function to return the response
    if shapes.count_documents({"id": shape_id}) > 0:
        shapes.replace_one({"id": shape_id}, shape.dict())
        return shape
    raise HTTPException(status_code=404, detail=f"No Shape with {shape_id} found")


@app.put("/shapes/upsert/{shape_id}")  # decorator to map the endpoint to the function
async def update_shape(shape_id: int, shape: Shape):  # function to return the response
    shapes.replace_one({"id": shape_id}, shape.dict(), upsert=True)
    return shape


@app.delete("/shapes/{shape_id}")  # decorator to map the endpoint to the function
async def delete_shape(shape_id: int):  # function to return the response
    delete_result = shapes.delete_one({"id": shape_id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"No Shape with {shape_id} found")
    return {"message": f"Shape ID {shape_id} deleted"}
