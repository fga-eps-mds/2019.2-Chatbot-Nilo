build-bot:
	./docker/build-base.sh
	make train

train:
	docker build . -f docker/coach.Dockerfile -t yukioz/coach
	docker-compose build bot

run-telegram:
	docker-compose up telegram_bot

run-console:
	docker-compose run bot make run-console

test-dialogue:
	docker-compose run --rm bot make e2e

test:
	docker-compose run --rm bot make test-stories