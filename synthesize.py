# Import AWS SDK for Python to connect AWS services
import boto3

with open('speech.txt', 'r') as file:
    text = file.read()
    print(text)

# Polly client creation
polly = boto3.client('polly')

# Requesting Polly to synthesize the text file 
response = polly.synthesize_speech(
    Engine='generative',
    OutputFormat='mp3',
    Text=text, # The text Polly is converting to speech
    VoiceId='Stephen' # Use the 'Stephen' voice for speech
)

# Extract the audio from the response
audioStream = response['AudioStream']

# Save the audio stream to a file name 'example.mp3'
with open("example.mp3", "wb") as f:
    f.write(audioStream.read()) # Read/Write the binary MP3 content to the example file
    print("Polly output saved.")