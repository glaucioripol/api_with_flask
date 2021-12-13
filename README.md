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

When created a new model is required import her on the [models](app/database/models/__init__.py) to become a migration

```bash
pipenv run migrate
```

# Interesing in develop it

- [ ] documentar swagger
- [ ] fazer testes
- [ ] pipeline jenkis oracle cloud
- [ ] deploy
