# Dataset Generation Process 
This repository stores the script that generates and exports the Measurements Dataset.

## Execution

To export the datasets, run the following command:

### Windows 

```bash
docker build -t dataset-hanagotchi -f Dockerfile . ; docker run --env-file .env dataset-hanagotchi ; docker rmi dataset-hanagotchi -f
```

### Linux / MacOS

```bash
make execute
```

## Enviroment Variables

- `POSTGRES_USER`: The user that will be used to connect to the database
- `POSTGRES_PASSWORD`: The password that will be used to connect to the database
- `POSTGRES_HOST`: The host where the database is located
- `POSTGRES_PORT`: The port where the database is listening
- `POSTGRES_DB`: The database name
- `DATABASE_URL`: The URL that will be used to connect to the database
- `MEASUREMENTS_SCHEMA`: The schema where the measurements table is located
- `PLANTS_SCHEMA`: The schema where the logs table is located

## Risks

- When a photo link does not follow the expected structure (the one followed by Firebase Storage), it could possibly not parse the created_at date as expected.