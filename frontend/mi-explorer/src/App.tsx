import React from 'react';
import './App.css';
import ThreeScene from './components/3dviewer/ThreeScene';
import FeatureDistribution from './components/3dviewer/FeatureDistribution';
import CrystalStructure from './components/3dviewer/CrystalStructure';
import TestBoxScene from './components/3dviewer/TestBoxScene';
import TestSphereScene from './components/3dviewer/TestSphereScene';


const App: React.FC = () => {
  return (
    <div className="App">
      {/* <Menu styles={styles} /> */}
      <CrystalStructure width={2000} height={1000} cameraPos={{x: 5, y: 5, z: 5}} />
    </div>
  );
}

export default App;
