import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles.css'; // Import the CSS file

// Define the shape of a chat message
interface ChatMessage {
  user: string;
  bot: string | null;
}

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [chatHistory, setChatHistory] = useState<ChatMessage[]>([]);

  const handleSend = async () => {
    if (!message) return;
    setResponse('Loading...');
    try {
      const res = await axios.post('http://localhost:5000/ask', { message });
      const botResponse = res.data.response || 'No response';
      setResponse(botResponse);
      setChatHistory([...chatHistory, { user: message, bot: botResponse }]);
      setMessage('');
    } catch (error) {
      setResponse('Error sending message');
      console.error(error);
    }
  };

  const loadHistory = async () => {
    try {
      const res = await axios.get('http://localhost:5000/memory');
      // Ensure the response data conforms to ChatMessage[]
      const history: ChatMessage[] = res.data.map((chat: any) => ({
        user: chat.user || '',
        bot: chat.bot || null,
      }));
      setChatHistory(history);
    } catch (error) {
      console.error('Error loading history:', error);
    }
  };

  const clearChat = async () => {
    try {
      await axios.delete('http://localhost:5000/memory');
      setChatHistory([]);
    } catch (error) {
      console.error('Error clearing chat:', error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div className="chat-container">
      <h1>Chatbot</h1>
      <div className="chat-history">
        {chatHistory.map((chat, index) => (
          <div key={index}>
            <strong className="user">You:</strong> {chat.user}<br />
            <strong className="bot">Bot:</strong> {chat.bot || 'No response'}<br /><br />
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button className="send-btn" onClick={handleSend}>Send</button>
        <button className="clear-btn" onClick={clearChat}>Clear Chat</button>
      </div>
      {response && <p className="response">Response: {response}</p>}
    </div>
  );
}

export default App;