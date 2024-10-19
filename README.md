# Pyrogram Webhook

## Overview

Pyrogram Webhook is a solution for setting up webhooks for Telegram bots using the Pyrogram library. Since Pyrogram does not natively support webhooks, this project leverages ngrok to create a public URL that can receive updates from Telegram. It also caches incoming requests in Redis for efficient processing.

## Features

- Set up a webhook for your Telegram bot using ngrok.
- Receive updates from Telegram servers in real-time.
- Cache incoming requests in Redis for improved performance and reliability.
- Easy to configure and deploy.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A Telegram bot token. You can create a bot by chatting with BotFather on Telegram.
- Ngrok installed and configured. You can download it from ngrok.com.
- Redis installed and running. You can find installation instructions on Redis's official website.

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/itpourya/pyrogram-webhook.git
   ```
3. Navigate to the project directory:
   ```bash
    cd pyrogram-webhook
   ```

## Usage

1. Run the application:
    ```bash
    pytyhon3 main.py
   ```
2. Your bot will now receive updates via the webhook set up with ngrok, and requests will be cached in Redis.

## Contribution

Feel free to contribute to this project by submitting pull requests:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
