import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/MenuHighlights.css';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const MenuHighlights = () => {
  const [menuItems, setMenuItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMenuItems = async () => {
      try {
        const response = await axios.get(`${API}/menu`);
        setMenuItems(response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching menu items:', err);
        setError('Failed to load menu items');
        setLoading(false);
      }
    };

    fetchMenuItems();
  }, []);

  if (loading) {
    return (
      <section id="menu" className="section menu-section">
        <div className="container">
          <div className="section-header">
            <h2>Popular Menu Highlights</h2>
            <p>Loading delicious menu items...</p>
          </div>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section id="menu" className="section menu-section">
        <div className="container">
          <div className="section-header">
            <h2>Popular Menu Highlights</h2>
            <p>{error}</p>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="menu" className="section menu-section">
      <div className="container">
        <div className="section-header">
          <h2>Popular Menu Highlights</h2>
          <p>Our most-loved dishes that keep customers coming back</p>
        </div>
        <div className="menu-grid">
          {menuItems.map((item) => (
            <div key={item._id} className="menu-card">
              <div className="menu-image">
                <img src={item.image} alt={item.name} />
              </div>
              <div className="menu-content">
                <h3>{item.name}</h3>
                <p>{item.description}</p>
                <div className="menu-price">${item.price}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default MenuHighlights;