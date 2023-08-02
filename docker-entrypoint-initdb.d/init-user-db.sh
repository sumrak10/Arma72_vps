#!/bin/bash
set -e

#	CREATE USER arma_bot_user WITH PASSWORD 'vErY26hhh03PSWD';
#	GRANT ALL PRIVILEGES ON DATABASE arma_bot_db TO arma_bot_user;

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE "$ARMA_BOT_DB_NAME";
EOSQL