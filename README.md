# block1 - Django REST Framework (Product API)

## Ishga tushirish (Git Bash)
    bash setup_and_test.sh

## Endpointlar
| Metod | URL | Vazifa |
|---|---|---|
| GET | /api/products/ | ro'yxat |
| POST | /api/products/ | yaratish |
| GET | /api/products/<id>/ | bitta mahsulot |
| PUT/PATCH | /api/products/<id>/ | yangilash |
| DELETE | /api/products/<id>/ | o'chirish |

## curl bilan sinash (server ishlayotganda, boshqa Git Bash oynasida)
    curl -X POST http://127.0.0.1:8000/api/products/ -H "Content-Type: application/json" -d '{"name":"Olma","price":"12000","description":"Yangi"}'
    curl http://127.0.0.1:8000/api/products/
    curl -X PATCH http://127.0.0.1:8000/api/products/1/ -H "Content-Type: application/json" -d '{"price":"13000"}'
    curl -X DELETE http://127.0.0.1:8000/api/products/1/
