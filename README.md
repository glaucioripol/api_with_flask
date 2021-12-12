# Api with flask and flask restful

To run that application, you need instal pipenv

## How to install dependencies

```bash
pipenv install
```

## How to run to dev

```bash
pipenv run dev
```

## update requirements

```bash
sh update_requirements.sh
```

## How to run migrations
you need create a model and add it in `migrations/env.py` your import as in that example

```python
from app.database.models.users import UsersModel
from app.database.models.spends import SpendsModel
from flask import current_app

from alembic import context
```

```bash
pipenv run migrate
```
