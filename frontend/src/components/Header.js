import React, { useState } from 'react';
import { Phone, Clock, Menu, X } from 'lucide-react';
import '../styles/Header.css';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMenuOpen(false);
    }
  };

  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <h2>Orphan Andy's</h2>
            <div className="header-badge">
              <Clock size={16} />
              <span>Open 24/7</span>
            </div>
          </div>

          <nav className={`nav ${isMenuOpen ? 'nav-open' : ''}`}>
            <button onClick={() => scrollToSection('about')}>About</button>
            <button onClick={() => scrollToSection('menu')}>Menu</button>
            <button onClick={() => scrollToSection('reviews')}>Reviews</button>
            <button onClick={() => scrollToSection('gallery')}>Gallery</button>
            <button onClick={() => scrollToSection('location')}>Location</button>
          </nav>

          <div className="header-actions">
            <a href="tel:+14158649795" className="btn-primary">
              <Phone size={18} />
              Call Now
            </a>
            <button 
              className="mobile-menu-btn"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;