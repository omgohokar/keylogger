import os
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
# Allow cross-origin requests so remote devices can connect securely
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

@socketio.on('connect')
def handle_connect():
    print("\n[CLOUD SERVER] Remote client session established.\nSTREAM: ", end="", flush=True)

@socketio.on('disconnect')
def handle_disconnect():
    print("\n---\n[CLOUD SERVER] Remote client disconnected.")

@socketio.on('client_stream')
def handle_client_stream(data):
    payload = data.get("payload", "")
    
    if payload == " [BACKSPACE] ":
        print("\b \b", end="", flush=True)
    else:
        print(payload, end="", flush=True)

if __name__ == '__main__':
    # FIX: Cloud providers inject the port dynamically. Fallback to 5000 if local.
    port = int(os.environ.get("PORT", 5000))
    
    # Bind to 0.0.0.0 so the server listens on all network interfaces
    print(f"[CLOUD SERVER] Starting network bridge on port {port}...")
    # Change the bottom section of server_bridge.py to this:

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"[CLOUD SERVER] Starting network bridge on port {port}...")
    
    # FIX: Added allow_unsafe_werkzeug=True
    socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)
