# Moex manager API for Python

moex-python-sdk - это внутренний проект для получения актуальных данных с Московской биржи.


# Установка через pip

```bash
pip install moex-python-sdk --trusted-host gitlab.rosbank.rus.socgen --index https://<username>:<password>@gitlab.rosbank.rus.socgen/api/v4/projects/335/packages/pypi/simple --trusted-host nexus.gts.rus.socgen --extra-index-url https://nexus.gts.rus.socgen/repository/pypi-org-proxy/simple/
```

где `<username>` - `__token__` и `<password>` - данные токена со скоупом `api`, который можно создать на данной странице: [https://gitlab.gts.rus.socgen/profile/personal_access_token]

Более подробная информация о токене: [https://docs.gitlab.com/ee/user/package/pypi_repository/#authenticating-with-a-personal-access-token]


# Как использовать SDK (poetry)

В самом начале нужно выполнить установку `poetry`. Так же на компьютере должна быть в наличии утилита `make` (в UNIX-системах, как правило идет в комплекте). Для установки в Windows можно воспользоваться менеджером пакетом `chokolatey`.

В своем проекте, в файл `pyproject.toml`, необходимо добавить указание, откуда собирать зависимости:

```toml
[[tool.poetry.source]]
name = "gitlab-package-registry"
url = "https:/gitlab.rosbank.rus.socgen/api/v4/projects/355/packages/pypi/simple"

```

После данной процедуры, нужно добавить данные учетной записи `gitlab` в `poetry`:

```bash
poetry config http-basic.gitlab-package-registry <username> <password>

```

где `<username>` - `__token__` и `<password>` - данные токена со скоупом `api`, который можно создать на данной странице: [https://gitlab.gts.rus.socgen/profile/personal_access_token]

Более подробная информация о токене: [https://docs.gitlab.com/ee/user/package/pypi_repository/#authenticating-with-a-personal-access-token]

Далее устанавливаем пакет в проект, как обычную зависимость:

```bash
poetry add moex-python-sdk --source gitlab-package-registry

```


# Как помочь

Установи [poetry]: https://python-poetry.org/docs/#installation

Следующим шагом, необходимо добавить proxy-репозиторий для корректной работы:

```bash
poetry source add --default nexus https://nexus.gts.rus.socgen/repository/pypi-org-proxy/simple/ 

```

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


# Чеклист на добавление нового функционала или изменение существующего

* Внести изменения
* Запустить тесты
* Поднять версию в pyproject.toml
* Отправить новую версию на сервер
* Дождаться окончания сборки и уведомить заинтересованных лиц об изменениях
