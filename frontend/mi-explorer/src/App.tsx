import React from 'react';
import './App.css';
import TestBoxScene from './components/3dviewer/TestBoxScene';
import Menu from './components/interface/Menu';
import Sidebar from "react-sidebar";
import ThreeScene from './components/3dviewer/ThreeScene';
import FeatureDistribution from './components/3dviewer/FeatureDistribution';


const App: React.FC = () => {
  return (
    <div className="App">
      {/* <Menu styles={styles} /> */}
      <FeatureDistribution width={2000} height={1000} cameraPos={{x: 5, y: 5, z: 5}} />
    </div>
  );
}

export default App;
