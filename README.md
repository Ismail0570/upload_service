# Upload-Service

## Запуск проекта
```bash
docker-compose up --build
```

## Эндпоинт загрузки файла
`POST /upload`

### Поддерживаемые форматы:
- JPG (image/jpeg)
- PNG (image/png)
- PDF (application/pdf)
- DICOM (application/dicom)

### Пример curl-запроса:
```bash
curl -X POST http://localhost:8000/upload \
  -F "file=@example.pdf"
```

## Swagger-документация
Открыть в браузере: [http://localhost:8000/docs](http://localhost:8000/docs)
