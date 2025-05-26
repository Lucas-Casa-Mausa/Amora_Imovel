import React from 'react';
import './App.css';
import Simulation from './components/Simulation';

const App = () => {
  return (
    <div className="App min-h-screen bg-gray-100 p-4">
      <header className="App-header mb-6">
        <h1 className="text-4xl font-bold">Simulação aMORA</h1>
      </header>
      <main>
        <Simulation />
      </main>
    </div>
  );
};

export default App;
