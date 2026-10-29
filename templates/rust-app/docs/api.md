---
title: API
nav_order: 2
---

# The API

{{name}} serves its API on the device itself: `{{name}} serve` listens on `http://127.0.0.1:{{api_port}}`, the web
app at `/`, the API under `/api/v1`. Requests and answers are JSON; an error is `{"error": "…"}` with a fitting
status.

The full description in OpenAPI is [`api/openapi.json`](https://github.com/{{name}}/{{name}}/blob/main/api/openapi.json)
– generated from the code by `{{name}} openapi`, and checked by CI to match it. A running server gives the same at
`/api/v1/openapi.json`.

| Method | Path | What |
|---|---|---|
| GET | `/api/v1/items` | every item |
| POST | `/api/v1/items` | adds an item: `{"title": "…"}` |
| DELETE | `/api/v1/items/{id}` | removes an item |
