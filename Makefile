build:
	docker build -t eaas .

non-async-build:
	docker build -t eaas_non_async -f non_async.Dockerfile .