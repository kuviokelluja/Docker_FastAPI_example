# FastAPI Docker Example

Demo of a FastAPI server dockerized to 3 stages

Sources are copied to **Development** on this demo, but in real environment you would add the sources as a **Volume** to **Development** and copy them over to **Builder** to allow developing without connection to your container

---

## Stage 1 - Development - 623MB

```build --target development -f "webserver.dockerfile" -t fastapiwebserver:latest "."```

## Stage 2 - Builder - 674MB

```build --target pyinstaller -f "webserver.dockerfile" -t fastapiwebserver:latest "."```

## Stage 3 - Production - 33.3MB

```build --target production -f "webserver.dockerfile" -t fastapiwebserver:latest "."```

### Running
After build:

```docker run -d -p 9999:9999 --name FastapiDemo fastapiwebserver tail -f /dev/null```

Compose to have each running on localhost:9997,9998,9999 respectively

```docker-compose --profile development --profile builder --profile production up```

