#!/bin/bash

# cd arma_bot
alembic revision --autogenerate -m "$REVISION_COMMENT"
alembic upgrade head
