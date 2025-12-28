import React from 'react';
import { MENU_ITEMS } from '../data/mockData';
import '../styles/MenuHighlights.css';

const MenuHighlights = () => {
  return (
    <section id="menu" className="section menu-section">
      <div className="container">
        <div className="section-header">
          <h2>Popular Menu Highlights</h2>
          <p>Our most-loved dishes that keep customers coming back</p>
        </div>
        <div className="menu-grid">
          {MENU_ITEMS.map((item, index) => (
            <div key={index} className="menu-card">
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