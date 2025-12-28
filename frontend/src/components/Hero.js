import React from 'react';
import { MapPin, Star } from 'lucide-react';
import '../styles/Hero.css';

const Hero = () => {
  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="hero">
      <div className="hero-overlay"></div>
      <div className="hero-image">
        <img 
          src="https://images.unsplash.com/photo-1761245193924-53a5a4bed9ef?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1Nzl8MHwxfHNlYXJjaHwxfHxjbGFzc2ljJTIwYW1lcmljYW4lMjBkaW5lcnxlbnwwfHx8fDE3NjY5MTU0ODB8MA&ixlib=rb-4.1.0&q=85" 
          alt="Orphan Andy's Restaurant"
        />
      </div>
      <div className="container hero-container">
        <div className="hero-content">
          <div className="hero-badge">
            <Star fill="#fbbf24" stroke="#fbbf24" size={20} />
            <span>4.5 (2,387 reviews)</span>
          </div>
          <h1>Open 24/7<br />Classic American Diner</h1>
          <p className="hero-subtitle">
            Serving delicious burgers, fluffy pancakes, creamy milkshakes, and all-American comfort food around the clock
          </p>
          <div className="hero-location">
            <MapPin size={20} />
            <span>3991 A 17th St, The Castro, San Francisco</span>
          </div>
          <div className="hero-actions">
            <button className="btn-primary" onClick={() => scrollToSection('menu')}>
              View Menu
            </button>
            <a 
              href="https://www.google.com/maps/dir//Orphan+Andy's+Restaurant,+3991+A+17th+St,+San+Francisco,+CA+94114" 
              target="_blank" 
              rel="noopener noreferrer"
              className="btn-secondary"
            >
              Get Directions
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;