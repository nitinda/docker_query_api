# docker_query_api
Hosting a website using Python flask (Development Mode) to received query and query an external api and displaying results.

---

## Usage

Running using Docker:

```bash
# FLASK_RUN_PORT Flask to run on desired port.
# API_DOMAIN - External domain with context path
# 

docker run --network="host" --rm -it -p 5001:5001 -e "FLASK_RUN_PORT=5001"  -e "API_DOMAIN=[http or https://<Domain>" nitindas/query-external-api:latest

```