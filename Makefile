default: Dockerfile

execute:
	docker build -t dataset-hanagotchi -f Dockerfile . && docker run --env-file .env -v ${PWD}/app/exports:/app/exports dataset-hanagotchi && docker rmi dataset-hanagotchi -f
.PHONY: execute