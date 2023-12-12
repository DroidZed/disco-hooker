<div align="center">
<h1>Disco Hooker</h1>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/leafengine/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Docker Image CI](https://github.com/DroidZed/disco-hooker/actions/workflows/docker-image.yml/badge.svg)](https://github.com/DroidZed/disco-hooker/actions/workflows/docker-image.yml)

</div>

<div>

## Intro

Thi is a simple Discord Hook notifier backend written in `flask` & `discord-webhook`.

![Example](/images/example.png)

## Usage:

1. Docker image:

   a. Pull the image:

   ```sh
   docker pull droidzed/disco-hooker:latest
   ```

   b. Run the container:

   ```sh
   docker run -d -p 6000:6000 -e PORT=6000 -e WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL droidzed/disco-hooker:latest
   ```

2. Run locally:

   a. Clone the repo:

   ```sh
   git clone https://github.com/DroidZed/disco-hooker.git
   ```

   b. Install deps:

   ```sh
   pipenv install
   ```

   c. Create `.env` file like so:
   <br>Make sure to fill in the required variables !

   ![env](./images/env.png)

   d. Run:

   ```sh
   py app.py
   ```

3. API Request:

   ![API Request](/images/request.png)

</div>

## Useful links:

[Discord Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
<br>[Discord Webhooks & Safety](https://discord.com/safety/using-webhooks-and-embeds)
