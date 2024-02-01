# Time.com Stories API

This repository contains two Python files for fetching the latest 6 stories from Time.com:

 - **Usage:**
     Make a GET request to http://127.0.0.1:5000/getTimeStories to get stories in JSON format.

     Example using cURL:
     ```bash
     curl http://127.0.0.1:5000/getTimeStories
     ```


1. **app.py (Scratch Implementation):**
   - **Run:**
     ```bash
     pip install Flask requests
     python app.py
     ```
  
2. **inbuilt.py (BeautifulSoup Implementation):**
   - **Run:**
     ```bash
     pip install requests beautifulsoup4
     python inbuilt.py
     ```
   - Fetches and displays the latest 6 stories using BeautifulSoup.

## Notes
- Flask (app.py) and BeautifulSoup (inbuilt.py) implementations.
- For educational purposes; may need adjustments based on specific use cases.
