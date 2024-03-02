#!/bin/bash
docker-compose -f prod.yaml up --build --remove-orphans -d
