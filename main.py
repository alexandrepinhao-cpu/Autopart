# API Endpoints

## Image Recognition
### Endpoint: `/api/image-recognition`
- **Method**: `POST`
- **Description**: Upload an image for recognition.
- **Request Body**: 
  - `image`: Base64 encoded image string.
- **Response**:
  - `200 OK`: Returns recognized object details.
  - `400 Bad Request`: Invalid image format.

## Web Scraping
### Endpoint: `/api/web-scraping`
- **Method**: `GET`
- **Description**: Scrape data from specified URL.
- **Query Parameters**:
  - `url`: The target URL to scrape.
- **Response**:
  - `200 OK`: Returns scraped data.
  - `404 Not Found`: URL not reachable.

## Price Comparison
### Endpoint: `/api/price-comparison`
- **Method**: `GET`
- **Description**: Compare prices for a given product.
- **Query Parameters**:
  - `product_id`: Unique identifier of the product.
- **Response**:
  - `200 OK`: Returns price comparison details.
  - `404 Not Found`: Product not found.

## Product Recommendations
### Endpoint: `/api/recommendations`
- **Method**: `GET`
- **Description**: Get product recommendations based on user preferences.
- **Query Parameters**:
  - `user_id`: Unique identifier for the user.
- **Response**:
  - `200 OK`: Returns a list of recommended products.
  - `404 Not Found`: No recommendations found.

## Search Functionality
### Endpoint: `/api/search`
- **Method**: `GET`
- **Description**: Search for products based on query.
- **Query Parameters**:
  - `query`: Search term.
- **Response**:
  - `200 OK`: Returns search results.
  - `400 Bad Request`: Invalid search term.

## Health Checks
### Endpoint: `/api/health`
- **Method**: `GET`
- **Description**: Check service health.
- **Response**:
  - `200 OK`: Service is healthy.
  - `500 Internal Server Error`: Service is down.

# Error Handling
- All endpoints should implement proper error handling to provide meaningful HTTP response codes and messages.

# Documentation
- Ensure that API documentation is updated as new endpoints are added or modified.