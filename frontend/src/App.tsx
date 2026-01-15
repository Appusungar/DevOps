import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const selectedFile = e.target.files[0];
      setFile(selectedFile);
      
      // Create preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result as string);
      };
      reader.readAsDataURL(selectedFile);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      // Change port if your backend runs on different port
      const response = await axios.post('http://localhost:8000/api/test-upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResult(response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
      setResult({ error: 'Upload failed!' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>VisionAI - Image Classifier</h1>
        <p>Upload an image to get started</p>
        
        <div style={{ margin: '20px' }}>
          <input 
            type="file" 
            accept="image/*" 
            onChange={handleFileChange}
            style={{ margin: '10px' }}
          />
          
          <button 
            onClick={handleUpload}
            disabled={!file || loading}
            style={{ 
              padding: '10px 20px',
              backgroundColor: file ? '#4CAF50' : '#ccc',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: file ? 'pointer' : 'not-allowed'
            }}
          >
            {loading ? 'Uploading...' : 'Upload Image'}
          </button>
        </div>

        {preview && (
          <div style={{ margin: '20px' }}>
            <h3>Preview:</h3>
            <img 
              src={preview} 
              alt="Preview" 
              style={{ maxWidth: '300px', maxHeight: '300px' }}
            />
          </div>
        )}

        {result && (
          <div style={{ 
            margin: '20px', 
            padding: '20px', 
            backgroundColor: '#f0f0f0',
            borderRadius: '10px',
            color: 'black',
            textAlign: 'left'
          }}>
            <h3>Upload Result:</h3>
            <pre>{JSON.stringify(result, null, 2)}</pre>
          </div>
        )}

        <div style={{ marginTop: '40px', fontSize: '14px', color: '#888' }}>
          <p>Week 1 Goal ✅: Frontend connects to Backend</p>
          <p>Next: Add actual image classification</p>
        </div>
      </header>
    </div>
  );
}

export default App;