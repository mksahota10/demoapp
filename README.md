# Flask RecallAI Messaging App

This Flask application integrates RecallAI's transcription functionality with a basic messaging platform. It provides routes for sending, retrieving, and recalling messages, as well as initiating a continuous transcription of a meeting.

## Functionalities

1. **Send Message**
   - Route: `/send_message` (POST)
   - Allows users to send a message to the messaging platform.
   - Use this route to send a message by providing a JSON payload with the message content.

2. **Get Messages**
   - Route: `/get_messages` (GET)
   - Retrieves all stored messages from the messaging platform.
   - Use this route to fetch all the messages stored within the application.

3. **Recall Message**
   - Route: `/recall_message` (DELETE)
   - Enables users to recall a specific message from the stored messages.
   - Use this route by providing the message to be recalled in a JSON payload.

4. **Transcribe Meeting**
   - Route: `/transcribe_meeting` (Server-Sent Events)
   - Initiates RecallAI's meeting transcription, providing continuous streaming of transcription data.
   - Use this route to start a meeting transcription. It streams the transcription data in real-time as Server-Sent Events.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Replace placeholders for RecallAI authentication token, meeting ID, and password with actual values in the Flask app.
4. Run the Flask app using `python app.py`.
5. Use tools like Postman or JavaScript to interact with the defined routes:
   - Send a message by making a POST request to `/send_message`.
   - Retrieve messages by sending a GET request to `/get_messages`.
   - Recall a message by issuing a DELETE request to `/recall_message`.
   - Access the continuous transcription by using a compatible SSE-enabled client to connect to `/transcribe_meeting`.

## Important Note

- Make sure to handle proper authentication and error handling for sensitive data and error scenarios.
- Refer to RecallAI's documentation for accurate usage and setup.
- Replace placeholder values with actual credentials for the Flask app and RecallAI to test the functionalities effectively.

Feel free to adapt and extend this README to suit your specific use case and audience.
