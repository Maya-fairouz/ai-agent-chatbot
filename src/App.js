import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  const handleSend = async () => {
    if (!message) return;
    setResponse('Loading...');
    try {
      const res = await axios.post('http://localhost:5000/ask', { message });
      setResponse(res.data.response || 'No response');
      setChatHistory([...chatHistory, { user: message, bot: res.data.response || 'No response' }]);
      setMessage('');
    } catch (error) {
      setResponse('Error sending message');
      console.error(error);
    }
  };

  const loadHistory = async () => {
    try {
      const res = await axios.get('http://localhost:5000/memory');
      setChatHistory(res.data);
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
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '20px' }}>Chatbot</h1>
      <div style={{ border: '1px solid #ccc', padding: '10px', marginBottom: '20px', height: '300px', overflowY: 'auto', backgroundColor: '#f9f9f9' }}>
        {chatHistory.map((chat, index) => (
          <div key={index} style={{ marginBottom: '10px' }}>
            <strong style={{ color: '#1e90ff' }}>You:</strong> {chat.user}<br />
            <strong style={{ color: '#32cd32' }}>Bot:</strong> {chat.bot || 'No response'}<br /><br />
          </div>
        ))}
      </div>
      <div style={{ display: 'flex', gap: '10px' }}>
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
          style={{ flex: '1', padding: '8px', border: '1px solid #ccc', borderRadius: '4px' }}
        />
        <button onClick={handleSend} style={{ padding: '8px 16px', backgroundColor: '#1e90ff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>Send</button>
        <button onClick={clearChat} style={{ padding: '8px 16px', backgroundColor: '#ff6347', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>Clear Chat</button>
      </div>
      {response && <p style={{ marginTop: '10px', color: '#555' }}>Response: {response}</p>}
    </div>
  );
}

export default App;