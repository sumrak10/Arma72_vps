#!/bin/bash

# arma_bot.alembic revision --autogenerate -m "init"
alembic -c arma_bot.ini upgrade head
