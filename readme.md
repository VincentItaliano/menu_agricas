# Menu scrapper
[![Pylint](https://github.com/VincentItaliano/menu_agricas/actions/workflows/pylint.yml/badge.svg?event=push)](https://github.com/VincentItaliano/menu_agricas/actions/workflows/pylint.yml)

## Installation
This repository has the following dependencies:
-   Requests (v2.31.0)
-   python-dotenv (v1.0.0)

you can install them in a virtual environnement using 
```bash
pip install -r requirements.txt
```
To use the telegram bot you need to create a ```.env``` file which contains your `BOT API KEY` and the `CHAT ID` of the chat where you want to send the menu.

```bash
BOT_TOKEN=<YOUR_BOT_TOKEN>
CHAT_ID=<YOUR_CHAT_ID>
```

## Usage 
Simply launch ```main.py``` to get the menu.
