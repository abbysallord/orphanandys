import React from 'react';
import { Store, ShoppingBag, Phone } from 'lucide-react';
import '../styles/Services.css';

const Services = () => {
  const services = [
    {
      icon: <Store size={32} />,
      title: 'Dine-In',
      description: 'Enjoy our cozy atmosphere and friendly service'
    },
    {
      icon: <ShoppingBag size={32} />,
      title: 'Takeaway',
      description: 'Grab your favorites to go, anytime 24/7'
    },
    {
      icon: <Phone size={32} />,
      title: 'Call Ahead',
      description: 'Order by phone at +1 415-864-9795'
    }
  ];

  return (
    <section className="section services-section">
      <div className="container">
        <div className="section-header">
          <h2>How to Enjoy Orphan Andy's</h2>
          <p>We make it easy to get your comfort food fix</p>
        </div>
        <div className="services-grid">
          {services.map((service, index) => (
            <div key={index} className="service-card">
              <div className="service-icon">{service.icon}</div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </div>
          ))}
        </div>
        <div className="service-note">
          <p>Wheelchair-accessible entrance available</p>
          <p>Price range: $10-20 per person</p>
        </div>
      </div>
    </section>
  );
};

export default Services;