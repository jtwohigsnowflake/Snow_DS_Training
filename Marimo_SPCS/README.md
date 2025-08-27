Psuedo instructions so far

# Deploying notebook to spcs

Assuming you have git and uv installed. uv is optional, regular python or other package managers are fine too. 

```sh
git clone https://github.com/sfc-gh-cromano/Snow_DS_Training
cd Snow_DS_Training
uv init
source .venv/bin/activate
uv add marimo snowflake snowflake-cli snowflake-snowpark-python
rm main.py # we do not need that
```

We have a Dockerfile

```txt
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 2718

CMD ["marimo", "edit", "notebook.py", "--host", "0.0.0.0", "--port", "2718", "--no-token"]
```

So we will need a compose file
```
services:
  marimo-in-snowflake:
    build:
      context: .
      dockerfile: Dockerfile
    image: ${SNOWFLAKE_ACCOUNT}.registry.snowflakecomputing.com/cube_testing/public/awesome_images/marimo-notebook:latest
    container_name: marimo-notebook
    ports:
      - "2718:2718"
    restart: unless-stopped
```
^^ the above “SNOWFLAKE_ACCOUNT” may not be needed, but I like to use it to docker push. 

`--no-token` is probably not a good idea. It should be okay because we’re in SPCS and prototyping for now without external access.

You will need docker installed or another virtualization solution like podman.

[Configure Snowflake CLI](https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-connections) and your virtualization solution to the account you want to deploy to where the default account matches “your-account” (

So we can now run:

```sh
export SNOWFLAKE_ACCOUNT=your-account
snow spcs image-registry login
docker compose build --push
```

If you want to try to connect inside Snowflake, here is this:

https://www.dataops.live/blog/connecting-to-snowflake-from-a-snowpark-container-services-spcs-container