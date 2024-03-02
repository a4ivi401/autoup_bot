# Автоматизированный бот для входа на форум Minecraft

Данный скрипт представляет собой автоматизированный бот, который входит на форум Minecraft, используя учетные данные, предоставленные внешним модулем `login_database_bot`. После входа на форум бот отправляет текстовое сообщение в определенную тему.

## Установка
Для работы скрипта требуется установить следующие зависимости:
- Selenium: `pip install selenium`

## Использование
1. Импортируйте необходимые модули:
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from datetime import datetime as dt, time as t
    import time
    import random
    from selenium.webdriver.chrome.options import Options
    from login_database_bot import login, passwrd
    ```

2. Настройте параметры браузера:
    ```python
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
    ```

3. Установите временные параметры для работы бота:
    ```python
    restart_time = random.randint(3600, 4000)
    current_time = dt.now().time()
    target_time = t(9, 0)
    ```

4. Запустите бесконечный цикл, который будет выполнять следующие действия:
    - Инициализация вебдрайвера
    - Вход на форум с использованием учетных данных
    - Отправка текстового сообщения в определенную тему на форуме
    - Завершение работы вебдрайвера
    - Ожидание до следующей итерации в зависимости от времени

## Примечание
- Бот ожидает, что внешний модуль `login_database_bot` предоставит переменные `login` и `passwrd` с учетными данными для входа на форум.
- Временные параметры `restart_time`, `current_time` и `target_time` используются для управления временными интервалами работы бота.
- В коде используется использование CSS селекторов и XPath для поиска элементов на веб-странице.
- После отправки сообщения бот завершает работу вебдрайвера и ожидает следующей итерации, в зависимости от текущего времени.
****

### Для работы бота вам необходимо установить Google Chrome
### Windows
   Перейдите на официальный сайт Google Chrome: https://www.google.com/chrome.
    Нажмите кнопку "Скачать Chrome".
    Запустите загруженный установочный файл.
    Следуйте инструкциям мастера установки.
    После завершения установки Google Chrome будет доступен в меню "Пуск" и на рабочем столе.

### Установка Google Chrome на Linux
### Ubuntu

   Откройте терминал.

   Добавьте ключ GPG Google Chrome:

	wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

Добавьте репозиторий Google Chrome в список источников программного обеспечения:

	sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

Обновите список пакетов:

	sudo apt update

Установите Google Chrome:

    sudo apt install google-chrome-stable

### Fedora и дистрибутивы на основе RPM:

Откройте терминал.

Добавьте репозиторий Google Chrome:

    sudo dnf install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

Установите Google Chrome:

    sudo dnf install google-chrome-stable

### Установка Google Chrome на macOS

*     Перейдите на официальный сайт Google Chrome: https://www.google.com/chrome.
*     Нажмите кнопку "Скачать Chrome".
*     Откройте загруженный диск-образ (.dmg) и перетащите значок Google Chrome в папку "Приложения".
*     Google Chrome будет установлен и будет доступен в папке "Приложения" на вашем Mac.

Теперь у вас должен быть установлен Google Chrome на вашей операционной системе.