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
## Authentication

### POST /api/auth/register

**Request body**
```json
{
  "username": "string",
  "password": "string",
  "role": "ADMIN | STAFF"
}
**Response**

- 201 Created (Đăng ký thành công)
```json
{
  "message": "Đăng ký thành công"
}
- 409 Conflict (Trùng username)
```json
{
  "message": "Username đã tồn tại"
}
- 400 Bad Request (Thiếu dữ liệu)
```json
{
  "message": "Thiếu username hoặc password"
}

