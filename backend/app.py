from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import Agent
from memory import Memory

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    agent = Agent()
    response = agent.get_response(data['message'])
    memory = Memory()
    memory.add_chat(data['message'], response)
    return jsonify({'response': response})

@app.route('/memory', methods=['GET'])
def get_memory():
    memory = Memory()
    chats = memory.get_chats()
    return jsonify([{'user': c.user_input, 'bot': c.bot_response} for c in chats])

@app.route('/memory', methods=['DELETE'])
def clear_memory():
    memory = Memory()
    memory.clear_chats()
    return jsonify({'message': 'Chat history cleared'})

if __name__ == '__main__':
    app.run(debug=True)