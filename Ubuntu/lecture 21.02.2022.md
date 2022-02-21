### RabbitMQ
#### RabbitMQ - это брокер сообщений с открытым кодом
Кратко работу RabbitMQ можно описать следующим образом:
1. Издатель отправляет сообщение определённому обменнику
2. Обменник, получив сообщение, маршрутизирует его в одну из нескольких очередей в соответствии с правилами привязки между ним и очередью
3. ОЧередь хранит ссилку на это сообщение. Само сообщение хранится в оперативной памяти или на диске
4. Как только потребитель готов получить сообщение из очереди на сервер создаёт копию сообщения по ссылке и отправляет
5. Потребитель получает сообщение и отправляет брокеру подтверждение
6. Брокер, получив подтверждение, удаляет копию сообщения очереди. Затем удаляет из оперативной памяти и с диска
### Docker (Докер)
#### Docker - программное обесеспечение с открытым исходным кодом, применяемое для разработки, тестирования, доставки и запуска веб-приложений в средах с поддержкой контейнирезации. 
Он нужен для более эффективного использование системы и ресурсов, быстрого развёртывания готовых программных продуктов, а также для их масшатаюировани и переноса в другие среды с гарантированным сохранением стабильной работы
**Компоненты Docker:**
1. Docker-демон - Сервер контейнеров, входящих в состав программных средств Docker
2. Docker-клиент - интерфейс взаимодействия пользователя с Docker- демоном
3. Docker -образ - файл, включающий зависимости, сведение, конфигурацию для дальнейшего развёртывания и инициализации контейнера
4. Docker-файл - описание правил по сборке образа, в котором первая строка указывает на базовый образ.
5. Docker-контейнер - это лёгкий, автономный исполняемый пакет программного обеспечения, который включает в себя всё необходимое для запуска приложения: код среду выполнения, системные инструменты, системные библиотеки и настройки
### Как работает Docker
1. Клиент отдаёт команду Docker`у-демону, развёрнутому на Docker-хосте.
2. Работа образа в контейнере. НАпример, запуск docker-image, посредством команды docker run bkb e;lfktybt rjybntqythf xthtp rjvfyle вщслук лшдд
### Что происходит при запуске контейнера
1. Происходит запуск образа (Docker-image).
2. DockerEngine проверяет существование образа. Если образ уже существует локально, Docker использует его для нового контейнера. При его отсутствии выполняется скачивание с Docker Hub
3. Создание контейнера из образа
4. Размера файловой системы и добавление слоя для записи
5. Создание сетевого интерфейса
6. Поиск и присвоение IP
### InfluxDB
БД временных рядов работают иначе. Для каждой точки, которую вы можете сохранить, у вас есть связанная с ней временная метка.
### Зачем нужны базы данных временных рядов?
Из-за многократной переиндексации данных производительность со временем снижается, при этом увеличивается нагрузка, что приводит к трудности при чтении данных.
База данных временных рядов оптимизирована для быстрого приёма данных. ТАкие системы используют индексацию данных, объединённых со временем. Как следствие, скрость загрузки не уменьшается со временем и остаётся достаточно стабильной