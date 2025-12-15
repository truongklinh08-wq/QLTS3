## GET /products
Response:
[
  {
    "id": 1,
    "name": "Trà sữa",
    "price": 25000
  }
]

## POST /invoices
Request:
{
  "items": [
    { "productId": 1, "quantity": 2 }
  ]
}
