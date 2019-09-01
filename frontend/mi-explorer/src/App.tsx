import React from 'react';
import './App.css';
import ThreeScene from './components/3dviewer/Three'


const App: React.FC = () => {
  return (
    <div className="App">
      <ThreeScene width={2000} height={1000} cameraPos={{x: 5, y: 5, z: 5}} />
    </div>
  );
}

export default App;
