import React from 'react';
import { MapPin, Phone, Clock, Facebook, Instagram, Twitter } from 'lucide-react';
import '../styles/Footer.css';

const Footer = () => {
  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-col">
            <h3>Orphan Andy's Restaurant</h3>
            <p>A San Francisco icon serving classic American diner fare since day one. Always open, always welcoming.</p>
            <div className="social-links">
              <a href="#" aria-label="Facebook">
                <Facebook size={20} />
              </a>
              <a href="#" aria-label="Instagram">
                <Instagram size={20} />
              </a>
              <a href="#" aria-label="Twitter">
                <Twitter size={20} />
              </a>
            </div>
          </div>
          <div className="footer-col">
            <h4>Quick Links</h4>
            <ul>
              <li><button onClick={() => scrollToSection('about')}>About Us</button></li>
              <li><button onClick={() => scrollToSection('menu')}>Menu</button></li>
              <li><button onClick={() => scrollToSection('reviews')}>Reviews</button></li>
              <li><button onClick={() => scrollToSection('gallery')}>Gallery</button></li>
              <li><button onClick={() => scrollToSection('location')}>Location</button></li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>Contact</h4>
            <ul className="contact-list">
              <li>
                <MapPin size={18} />
                <span>3991 A 17th St, San Francisco, CA 94114</span>
              </li>
              <li>
                <Phone size={18} />
                <a href="tel:+14158649795">+1 415-864-9795</a>
              </li>
              <li>
                <Clock size={18} />
                <span>Open 24/7</span>
              </li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>Hours</h4>
            <div className="hours-list">
              <div className="hours-item">
                <span>Monday - Sunday</span>
                <span className="hours-badge">24 Hours</span>
              </div>
              <p className="hours-note">We never close! Visit us anytime.</p>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} Orphan Andy's Restaurant. All rights reserved.</p>
          <p className="footer-links">
            <a href="#">Privacy Policy</a>
            <span>•</span>
            <a href="#">Terms of Service</a>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;