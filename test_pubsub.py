from google.cloud import pubsub_v1
import os

# Ensure the GOOGLE_APPLICATION_CREDENTIALS environment variable is set.
# You should have set it in the previous step like so:
# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\jcirillo\Desktop\Zeta\your-service-account-file.json

# Define your project ID and topic name
project_id = "zeta-437623"  # Your Google Cloud project ID
topic_id = "Zeta-Topic"     # Replace with your Pub/Sub topic name as seen in the screenshot

def publish_message(project_id, topic_id, message):
    # Create a Publisher client
    publisher = pubsub_v1.PublisherClient()
    # Create the fully qualified topic path
    topic_path = publisher.topic_path(project_id, topic_id)

    # Publish a message to the topic
    future = publisher.publish(topic_path, message.encode("utf-8"))
    print(f"Published message ID: {future.result()}")

if __name__ == "__main__":
    # Test message to send
    message = "This is a test message from Pub/Sub!"
    
    # Publish the message
    try:
        publish_message(project_id, topic_id, message)
        print("Message published successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
