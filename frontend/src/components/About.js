import React from 'react';
import { Clock, Award, Users } from 'lucide-react';
import '../styles/About.css';

const About = () => {
  return (
    <section id="about" className="section about-section">
      <div className="container">
        <div className="about-content">
          <div className="about-text">
            <h2>Welcome to Orphan Andy's</h2>
            <p>
              Since our doors first opened in The Castro, Orphan Andy's has been serving up 
              classic American comfort food with a side of community warmth. Our old-school 
              diner is a San Francisco institution, beloved by locals and visitors alike.
            </p>
            <p>
              Open 24 hours a day, 7 days a week, we're here whenever hunger strikes. Whether 
              it's a hearty breakfast after a long night, a satisfying lunch, or a late-night 
              burger craving, Orphan Andy's delivers authentic diner fare made with care.
            </p>
            <p>
              With over 2,387 five-star reviews and a 4.5-star rating, our reputation speaks 
              for itself. Join the thousands who've made us their go-to spot for pancakes, 
              milkshakes, and everything in between.
            </p>
          </div>
          <div className="about-features">
            <div className="feature-card">
              <div className="feature-icon">
                <Clock size={32} />
              </div>
              <h3>Always Open</h3>
              <p>24/7 service means we're ready whenever you are</p>
            </div>
            <div className="feature-card">
              <Award size={32} />
              <h3>Award-Winning</h3>
              <p>4.5 stars from over 2,387 satisfied customers</p>
            </div>
            <div className="feature-card">
              <Users size={32} />
              <h3>Community Hub</h3>
              <p>A Castro neighborhood favorite since day one</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;