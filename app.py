from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/getTimeStories')
def get_time_stories():
    url = "https://time.com"
    response = requests.get(url)
    html_content = response.text

    stories = []

    # Find the latest stories section
    start_index = html_content.find('<div class="partial latest-stories"')
    end_index = html_content.find('</ul>', start_index)

    latest_stories_section = html_content[start_index:end_index]

    # Extract the latest 6 stories
    for _ in range(6):
        start_index = latest_stories_section.find('<a href="', start_index) + 9
        end_index = latest_stories_section.find('</a>', start_index)
        title_start = latest_stories_section.find('<h3', start_index)
        title_start = latest_stories_section.find('>', title_start) + 1
        title_end = latest_stories_section.find('</h3>', title_start)
        title = latest_stories_section[title_start:title_end].strip()

        link_start = latest_stories_section.find('href="', start_index) + 6
        link_end = latest_stories_section.find('"', link_start)
        link = url + latest_stories_section[link_start:link_end]

        # Construct the dictionary in the desired order
        story_dict = {'title': title, 'link': link}
        stories.append(story_dict)

        start_index = end_index

    # Use json.dumps for a more systematic JSON response
    json_response = jsonify(stories)

    return json_response

if __name__ == "__main__":
    app.run(debug=True)
