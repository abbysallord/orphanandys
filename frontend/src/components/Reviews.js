import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Star } from 'lucide-react';
import '../styles/Reviews.css';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const Reviews = () => {
  const [reviewStats, setReviewStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchReviewStats = async () => {
      try {
        const response = await axios.get(`${API}/reviews/stats`);
        setReviewStats(response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching review stats:', err);
        setLoading(false);
      }
    };

    fetchReviewStats();
  }, []);

  if (loading || !reviewStats) {
    return (
      <section id="reviews" className="section reviews-section">
        <div className="container">
          <div className="section-header">
            <h2>What Customers Say</h2>
            <p>Loading reviews...</p>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="reviews" className="section reviews-section">
      <div className="container">
        <div className="section-header">
          <h2>What Customers Say</h2>
          <p>Join thousands of satisfied diners</p>
        </div>
        <div className="reviews-content">
          <div className="reviews-summary">
            <div className="rating-overview">
              <div className="rating-number">{reviewStats.average}</div>
              <div className="rating-stars">
                {[1, 2, 3, 4, 5].map((star) => (
                  <Star
                    key={star}
                    size={24}
                    fill={star <= Math.floor(reviewStats.average) ? '#fbbf24' : 'none'}
                    stroke="#fbbf24"
                  />
                ))}
              </div>
              <div className="rating-count">{reviewStats.total.toLocaleString()} reviews</div>
            </div>
            <div className="rating-breakdown">
              {reviewStats.breakdown.map((item) => (
                <div key={item.stars} className="rating-bar">
                  <span className="rating-label">{item.stars} ★</span>
                  <div className="bar-container">
                    <div className="bar-fill" style={{ width: `${item.percentage}%` }}></div>
                  </div>
                  <span className="rating-count">{item.count}</span>
                </div>
              ))}
            </div>
          </div>
          <div className="popular-keywords">
            <h3>Popular Mentions</h3>
            <div className="keywords-grid">
              {reviewStats.popularKeywords.map((keyword, index) => (
                <div key={index} className="keyword-tag">
                  <span className="keyword-word">{keyword.word}</span>
                  <span className="keyword-count">{keyword.count}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Reviews;