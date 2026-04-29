from pyngrok import ngrok
import time

# Connect to the local Flask app running on port 5000
public_url = ngrok.connect(5000)
print(f"\n=======================================================")
print(f"YOUR PUBLIC URL: {public_url.public_url}")
print(f"=======================================================\n")

try:
    # Block until CTRL-C or some other terminating event
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down ngrok...")
    ngrok.kill()
