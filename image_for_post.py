import prompts
import anthropic

def responseToImage():
    # stores the response.txt contents in response
    with open('response.txt', 'r') as f:
        response = f.read()

    # uses convertResponseToImage fucntion from prompt.py to genreate prompt for Claude AI
    image_prompt = prompts.convertResponseToImage(response)

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": image_prompt}
        ]
    )
    
    # stores response from Claude AI into a .svg file
    image = message.content[0].text
    with open('image.svg', 'w') as file:
        file.write(str(image))

responseToImage()