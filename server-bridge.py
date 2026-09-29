from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
# Keep async_mode='threading' to avoid multi-thread locking on Windows 11
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

@socketio.on('connect')
def handle_connect():
    print("\n[SERVER] Client connected. Incoming stream will print below:\n---")

@socketio.on('disconnect')
def handle_disconnect():
    print("\n---\n[SERVER] Client disconnected.")

# Cleaned up event listener: strictly receives data and outputs to terminal
@socketio.on('client_stream')
def handle_client_stream(data):
    payload = data.get("payload", "")
    
    if payload == " [BACKSPACE] ":
        # Move console cursor back, blank out the character, and step back again
        print("\b \b", end="", flush=True)
    else:
        # Stream the characters next to each other horizontally
        print(payload, end="", flush=True)

if __name__ == '__main__':
    print("[SERVER] Listening for client applications on port 5000...")
    socketio.run(app, host='127.0.0.1', port=5000)
