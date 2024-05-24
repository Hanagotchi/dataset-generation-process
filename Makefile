default: Dockerfile

execute:
	docker build -t dataset-hanagotchi -f Dockerfile . && docker run --env-file .env dataset-hanagotchi && docker rmi dataset-hanagotchi -f
.PHONY: execute