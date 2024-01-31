import React from 'react';
import Torneo from './components/Torneig.js';
import './App.css';

import connect from '../../server/db/index.js';
import sequelize from '../../server/db/conf.js';

connect();

function App() {
  return (
    <div className="App">
      <Torneo />
    </div>
  );
}

export default App;