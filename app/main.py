from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
	return {"message": "ok!"}
	# uncomment the line below to see hot reload in action
	# return {"message": "hot reload!"}
