import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [audioUrl, setAudioUrl] = useState('');

  useEffect(() => {
    const fetchAudio = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/', { responseType: 'blob' });
        const blob = new Blob([response.data], { type: 'audio/mp3' });
        setAudioUrl(URL.createObjectURL(blob));
      } catch (error) {
        console.error('Error fetching audio', error);
      }
    };
    fetchAudio();
  }, []);

  const audioContainerStyle = {
    width: '200px', // Adjust the width of the audio container
  };

  const audioStyle = {
    width: '500%', // Set the width of the audio player to 100%
  };

  return (
    <div style={audioContainerStyle}>
      {audioUrl && (
        <audio autoPlay controls controlsList="nodownload noplaybackrate nofullscreen" style={audioStyle} src={audioUrl}>
          Your browser does not support the audio element.
        </audio>
      )}
    </div>
  );
};

export default App;

