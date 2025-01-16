import requests

def download_image(image_url, file_name):
    response = requests.get(image_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

# Download button images
download_image('https://media.geeksforgeeks.org/wp-content/uploads/20240610151926/play.png', 'play.png')
download_image('https://media.geeksforgeeks.org/wp-content/uploads/20240610151926/pause.png', 'pause.png')
download_image('https://media.geeksforgeeks.org/wp-content/uploads/20240610151926/next.png', 'next.png')
download_image('https://media.geeksforgeeks.org/wp-content/uploads/20240610151926/previous.png', 'previous.png')
