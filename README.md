# Deeplogic-tech

# Time.com Stories API

This Flask application serves as a simple API to retrieve the latest 6 stories from Time.com by parsing the HTML of the page.

## Prerequisites

- Python 3.x
- Flask
- Requests

## Setup

1. Install the required dependencies:

    ```bash
    pip install Flask requests
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

   This will start the server on http://127.0.0.1:5000/.

## Usage

Make a GET request to http://127.0.0.1:5000/getTimeStories to retrieve the latest 6 stories in the specified JSON format.

Example using cURL:

```bash
curl http://127.0.0.1:5000/getTimeStories
