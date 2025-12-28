import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Clock } from 'lucide-react';
import '../styles/BusyTimes.css';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const BusyTimes = () => {
  const [busyTimes, setBusyTimes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBusyTimes = async () => {
      try {
        const response = await axios.get(`${API}/busy-times`);
        setBusyTimes(response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching busy times:', err);
        setLoading(false);
      }
    };

    fetchBusyTimes();
  }, []);

  if (loading || busyTimes.length === 0) {
    return (
      <section className="section busy-times-section">
        <div className="container">
          <div className="section-header">
            <Clock size={40} />
            <h2>Best Times to Visit</h2>
            <p>Loading busy times data...</p>
          </div>
        </div>
      </section>
    );
  }

  const maxValue = Math.max(...busyTimes.map(t => t.value));

  return (
    <section className="section busy-times-section">
      <div className="container">
        <div className="section-header">
          <Clock size={40} />
          <h2>Best Times to Visit</h2>
          <p>Plan your visit around our typical crowd levels</p>
        </div>
        <div className="busy-times-chart">
          {busyTimes.map((time, index) => (
            <div key={index} className="time-bar">
              <div className="time-label">{time.hour}</div>
              <div className="bar-wrapper">
                <div 
                  className="bar" 
                  style={{ height: `${(time.value / maxValue) * 100}%` }}
                >
                  <span className="bar-value">{time.value}%</span>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="busy-times-info">
          <div className="info-card">
            <h4>Busiest Hours</h4>
            <p>12 PM - 1 PM</p>
          </div>
          <div className="info-card">
            <h4>Quietest Hours</h4>
            <p>3 AM - 5 AM</p>
          </div>
          <div className="info-card highlight">
            <h4>Open 24/7</h4>
            <p>Visit anytime that suits you!</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default BusyTimes;