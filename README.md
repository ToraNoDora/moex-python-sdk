# Moex manager API for Python

moex-python-sdk - это проект для получения актуальных данных с Московской биржи (https://iss.moex.com).


# Установка через pip

```bash
pip install moex-python-sdk
```

# Как использовать SDK (poetry)

В самом начале нужно выполнить установку `poetry`. Так же на компьютере должна быть в наличии утилита `make` (в UNIX-системах, как правило идет в комплекте). Для установки в Windows можно воспользоваться менеджером пакетом `chokolatey`.

В своем проекте, в файл `pyproject.toml`, необходимо добавить указание, откуда собирать зависимости:

```toml
[[tool.poetry.source]]
name = "your-package-registry"
url = url-package-registry"

```

После данной процедуры, нужно добавить данные учетной записи `your-package-registry` в `poetry`:

```bash
poetry config http-basic.your-package-registry <username> <password>

```

Далее устанавливаем пакет в проект, как обычную зависимость:

```bash
poetry add moex-python-sdk --source your-package-registry

```


# Как помочь

Установи [poetry]: https://python-poetry.org/docs/#installation

Выполни:

    $ make init

чтобы установить зависимости. После этого можно приступать к работе, предварительно выполнив прогон тестов:

    $ make test


# Пример использования

```py
from moex_python_sdk import Moex

moex_api = Moex()

# если необходим прокси при подключение 
moex_api.connection_with_proxy()

current_ = moex_api.api(). #
current_ = moex_api. #

```

