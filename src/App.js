import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Navbar from './components/Navbar';
import HomePage from './components/HomePage';
import PlanFinder from './components/PlanFinder';
import Dashboard from './components/Dashboard';
import About from './components/About';
import './index.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/plans" element={<PlanFinder />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <Toaster position="top-right" />
      </div>
    </Router>
  );
}

export default App; 