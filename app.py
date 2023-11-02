from flask import Flask, Response, stream_with_context, jsonify, request
from recallai import RecallAi

app = Flask(__name__)

messages = []  # Placeholder for stored messages
client = RecallAi(auth_token="YOUR_RECALLAI_AUTH_TOKEN")  # Initialize RecallAI client with your auth token

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()  # Retrieve message from the POST request
    message = data.get('message')  # Extract the message
    messages.append(message)  # Add the message to the messages list
    return jsonify({"message": "Message sent successfully"})  # Return a success message in JSON format

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})  # Return the stored messages in JSON format upon a GET request

@app.route('/recall_message', methods=['DELETE'])
def recall_message():
    data = request.get_json()  # Get the message to recall from the DELETE request
    message_to_recall = data.get('message')  # Extract the message to be recalled
    if message_to_recall in messages:  # Check if the message exists in the stored messages
        messages.remove(message_to_recall)  # Remove the message if found
        return jsonify({"message": "Message recalled"})  # Return a success message in JSON format
    else:
        return jsonify({"message": "Message not found"})  # Return a message if the requested message is not found

@app.route('/transcribe_meeting')
def transcribe_meeting():
    def generate():
        bot = client.send_bot_to_meeting(
            platform="zoom",  # Replace with the actual platform (e.g., Zoom, Google Meet)
            meeting_id="YOUR_MEETING_ID",  # Replace with the specific meeting ID
            meeting_password="YOUR_MEETING_PASSWORD",  # Replace with the password for the meeting
        )

        for part in bot.stream_transcription():
            yield f"data: {part.speaker}: {part.text}\n\n"  # Stream transcription data as Server-Sent Events (SSE)

    return Response(stream_with_context(generate()), content_type='text/event-stream')  # Continuous streaming of transcription data

if __name__ == '__main__':
    app.run(debug=True)




