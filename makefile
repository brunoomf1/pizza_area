run:
	uvicorn api:app --reload --port 5000 --log-config logs/log_config.yml --env-file db.config --access-log 
