# Perevals API

Проект "Perevals" представляет собой REST API для управления данными о перевалах. Он позволяет пользователям добавлять, получать и редактировать информацию о перевалах. Проект опубликован на хостинге BEGET.com и доступен по адресу https://lebedev-project.ru/api/perevals.

## Основные функции

 **Получение списка перевалов**:  
 - GET /api/perevals
 - Ответ: Список всех перевалов в формате JSON.

**Получение списка перевалов пользователя по email**:
```http
GET /api/perevals/?user_id__email=<email>

```     
Ответ: Список перевалов в формате JSON
     
 **Добавление нового перевала**:  
   - POST /api/perevals
   - Пример запроса: JSON с данными о перевале:
      ```json
           {  
            "beauty_title": "ПЕРЕВАЛ",
            "title": "ПЕРЕВАЛ",
            "other_titles": "ПЕРЕВАЛ",
            "connect": "rtgr",
            "add_time": "2021-09-22T13:18:13",
            "user": {
                "email": "test@test.com",
                "fam": "user",
                "name": "user",
                "otc": "user",
                "phone": "8900000056"
            },
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"
            },
            "level": {
                "winter": "1B",
                "summer": "1B",
                "autumn": "1B",
                "spring": "1B"
            },
            "images": [
                {
                    "data": "КАРТИНКА1",
                    "title": "ЗАГОЛОВОК1"
                },
                {
                    "data": "КАРТИНКА2",
                    "title": "ЗАГОЛОВОК2"
                }
            ]
        }
      ```
       
   - Ответ:  
     - В случае успешного сохранения перевала:  
       ```json
       {
           "status": 200,"message": "Отправлено успешно",
           "id": "<id перевала>"
       }
       ```  
     - В случае ошибки:  
       ```json
       {
           "status": 400,
           "message": "Некорректные данные",
           "errors": "<список ошибок>"
       }
       ```

 **Получение информации о конкретном перевале**:  
   - GET /api/perevals/<id>
   - Ответ: Информация о перевале в формате JSON.

 **Редактирование перевала**:  
   - PATCH /api/perevals/<id>
   - Тело запроса: JSON с обновленными данными о перевале  
   - Ответ:  
     - В случае успешного обновления:  
       ```json
       {
           "status": 1,
           "message": "Перевал успешно обновлен"
       }
       ```  
     - В случае ошибки:  
       ```json
       {
           "status": 0,
           "message": "Некорректные данные",
           "errors": "<список ошибок>"
       }
       ```
     - В случае обновления данных пользователя:
      ```json
       {
            "state": 0,
             "message": "нельзя менять данные пользователя"
       }
      
       ```
      - При попытке обновить перевал в статусе отлично от "new":
       ```json
       {
            "state": 0,
             "message": "Изменять запись можно только в статусе 'new'"
       }
       ```

## Документация

1. **Swagger**:  
   - Адрес: https://lebedev-project.ru/swagger  
   - Описание: Интерфейс для просмотра и тестирования API.

2. **DRF документация**:  
   - Адрес: https://lebedev-project.ru/api  
   - Описание: Документация API, сгенерированная с помощью Django REST Framework.

## Настройка проекта

1. **Файл `.env`**:  
   - В проекте есть файл `env.example`, который нужно переименовать в `.env` и подставить в переменные свои значения.  
   - Пример:  
     ```bash
     FSTR_DB_HOST=your_database_host
     FSTR_DB_PORT=your_database_port
     FSTR_DB_LOGIN=your_database_login
     DATABASE_NAME=your_database_name
     FSTR_DB_PASS=your_database_password
     MY_API_KEY=your_api_key
     ```

2. **Создание виртуального окружения**:  
   - Создайте виртуальное окружение:  
     ```bash
     python -m venv venv
     ```
   - Активируйте его:  
     ```bash
     source venv/bin/activate  # Для Linux/Mac
     venv\Scripts\activate      # Для Windows
     ```

3. **Установка зависимостей**:  
   - Установите зависимости с помощью `pip`:  
     ```bash
     pip install -r requirements.txt
     ```
     ```

4. **Запуск проекта**:  
   - Запустите сервер разработки:  
     ```bash
     python manage.py runserver
     ```

## Заключение

Проект "Perevals" предоставляет удобный и мощный API для управления данными о перевалах. Он легко настраивается и может быть расширен в будущем.