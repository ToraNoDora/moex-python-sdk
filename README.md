# Moex manager API for Python

little-moex - небольшой проект для получения актуальных данных с Московской биржи (https://iss.moex.com).


## Как использовать SDK (poetry)

В своем проекте, в файл `pyproject.toml`, необходимо добавить указание, откуда собирать зависимости:

```toml
[[tool.poetry.source]]
name = "your-package-registry"
url = "url-package-registry"

```

После нужно добавить данные учетной записи `your-package-registry` в `poetry`:

```bash
$ poetry config http-basic.your-package-registry <username> <password>
```

Далее устанавливаем пакет в проект, как обычную зависимость:

```bash
$ poetry add little-moex --source your-package-registry
```


## Как помочь

Установи [poetry]: https://python-poetry.org/docs/#installation

```bash
$ make init
```
чтобы установить зависимости. После этого можно приступать к работе, предварительно выполнив прогон тестов:

```bash
$ make test
```

## Пример

```py
from moex_python_sdk import Moex
from moex_python_sdk.models.index import new_index_params


moex_api = Moex()
index_api = moex_api.index()

params = new_index_params()
index = index_api.get_index(params)["content"]

print(index["markets"])
```

