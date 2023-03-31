# Shapemaker

Geospatial geometry storage and retrieval

## Usage

### Set Up the Database

Install 

```shell
poetry install --with migration
```

Apply migrations:

```shell
poetry run alembic upgrade head
```

### Launch the service

```shell

```

## Development

Install development dependencies:

```shell
poetry install --with dev
```

### Serving

```shell
poetry run uvicorn shapemaker:main \
--app-dir src/ \
--factory \
--reload
```

### Testing

Run the test suite:

```shell
poetry run pytest
```

Check code coverage:

```shell
poetry run pytest --cov
```

Generate a browsable coverage report:

```shell
poetry run pytest --cov --cov-report html
```

### Linting

Run linter:

```shell
poetry run flake8
```

> Code formatting errors can usually be fixed by running `black`:
>
> ```shell
> poetry run black src/
> ```

### Building

Build source and wheel distributions:

```shell
poetry build
```

> This will output build artifacts to `dist/`.
