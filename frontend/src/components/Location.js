import React from 'react';
import { MapPin, Phone, Clock, Globe } from 'lucide-react';
import '../styles/Location.css';

const Location = () => {
  return (
    <section id="location" className="section location-section">
      <div className="container">
        <div className="section-header">
          <h2>Visit Us</h2>
          <p>We're in the heart of The Castro, San Francisco</p>
        </div>
        <div className="location-content">
          <div className="location-info">
            <div className="info-item">
              <div className="info-icon">
                <MapPin size={24} />
              </div>
              <div className="info-text">
                <h4>Address</h4>
                <p>3991 A 17th St<br />San Francisco, CA 94114</p>
                <a 
                  href="https://www.google.com/maps/dir//Orphan+Andy's+Restaurant,+3991+A+17th+St,+San+Francisco,+CA+94114" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="location-link"
                >
                  Get Directions →
                </a>
              </div>
            </div>
            <div className="info-item">
              <div className="info-icon">
                <Phone size={24} />
              </div>
              <div className="info-text">
                <h4>Phone</h4>
                <a href="tel:+14158649795" className="phone-link">+1 415-864-9795</a>
                <p className="small-text">Call ahead for takeaway orders</p>
              </div>
            </div>
            <div className="info-item">
              <div className="info-icon">
                <Clock size={24} />
              </div>
              <div className="info-text">
                <h4>Hours</h4>
                <p className="highlight-text">Open 24 Hours</p>
                <p className="small-text">7 Days a Week</p>
              </div>
            </div>
            <div className="info-item">
              <div className="info-icon">
                <Globe size={24} />
              </div>
              <div className="info-text">
                <h4>Website</h4>
                <a href="https://orphanandys.site" target="_blank" rel="noopener noreferrer" className="location-link">
                  orphanandys.site
                </a>
              </div>
            </div>
          </div>
          <div className="location-map">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.7127817538567!2d-122.43514492346205!3d37.76256077197522!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808f7e3e1c7c7c7f%3A0x7c7c7c7c7c7c7c7c!2s3991%2017th%20St%2C%20San%20Francisco%2C%20CA%2094114!5e0!3m2!1sen!2sus!4v1640000000000!5m2!1sen!2sus"
              width="100%"
              height="100%"
              style={{ border: 0, borderRadius: 'var(--border-radius-lg)' }}
              allowFullScreen=""
              loading="lazy"
              referrerPolicy="no-referrer-when-downgrade"
              title="Orphan Andy's Restaurant Location"
            ></iframe>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Location;