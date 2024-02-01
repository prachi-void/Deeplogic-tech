from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__,static_url_path='/static')

def get_latest_stories():
    try:
        response = requests.get('https://time.com/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            latest_stories = []
            for li in soup.select('.latest-stories__item'):
                headline = li.select_one('.latest-stories__item-headline').text.strip()
                link = li.select_one('a')['href']
                timestamp = li.select_one('.latest-stories__item-timestamp').text.strip()

                latest_stories.append({
                    'headline': headline,
                    'link':'https://time.com'+ link
                })

            return latest_stories

        else:
            return [{'error': f"Unable to fetch data from Time.com. Status Code: {response.status_code}"}]

    except Exception as e:
        return [{'error': str(e)}]

@app.route('/getTimeStories', methods=['GET'])
def getTimeStories():
    stories = get_latest_stories()
    return jsonify(stories)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

