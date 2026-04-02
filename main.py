from fastapi import FastAPI

app = FastAPI()

@app.get("/image-recognition")
async def image_recognition(image_url: str):
    return {"message": "Image recognition endpoint", "image_url": image_url}

@app.get("/web-scraping")
async def web_scraping(url: str):
    return {"message": "Web scraping endpoint", "url": url}

@app.get("/price-comparison")
async def price_comparison(product_id: str):
    return {"message": "Price comparison endpoint", "product_id": product_id}

@app.get("/product-recommendations")
async def product_recommendations(user_id: str):
    return {"message": "Product recommendations endpoint", "user_id": user_id}