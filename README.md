# Time.com Stories API

This repository contains two Python files for fetching the latest 6 stories from Time.com using different approaches: 
one from scratch and the other using BeautifulSoup for parsing.

## Prerequisites

- Python 3.x
- Flask (for app.py)
- Requests (for app.py)
- BeautifulSoup (for inbuilt.py)

## Setup

### For app.py (Scratch Implementation)

1. Install the required dependencies:

    ```bash
    pip install Flask requests
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

   This will start the server on http://127.0.0.1:5000/.

### For inbuilt.py (BeautifulSoup Implementation)

1. Install the required dependencies:

    ```bash
    pip install requests beautifulsoup4
    ```

2. Run the Python script:

    ```bash
    python inbuilt.py
    ```

## Usage

### Using app.py (Scratch Implementation)

Make a GET request to http://127.0.0.1:5000/getTimeStories to retrieve the latest 6 stories in the specified JSON format.

Example using cURL:

```bash
curl http://127.0.0.1:5000/getTimeStories```


Using inbuilt.py (BeautifulSoup Implementation)
Run the Python script:

python inbuilt.py
The script will fetch and display the latest 6 stories using BeautifulSoup.

Notes
Ensure that the Flask application (app.py) is running before making requests.

Both implementations use basic HTML parsing, and any changes to the structure of Time.com may impact the parsing logic.

These examples are for educational purposes and may require adjustments based on specific use cases.


This README now includes information about both app.py (from scratch) and inbuilt.py (using BeautifulSoup) scripts. Adjustments might be necessary based on your specific project structure or requirements.
