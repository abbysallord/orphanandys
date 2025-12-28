import React from 'react';
import { Star } from 'lucide-react';
import { REVIEWS_STATS, POPULAR_KEYWORDS } from '../data/mockData';
import '../styles/Reviews.css';

const Reviews = () => {
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
              <div className="rating-number">{REVIEWS_STATS.average}</div>
              <div className="rating-stars">
                {[1, 2, 3, 4, 5].map((star) => (
                  <Star
                    key={star}
                    size={24}
                    fill={star <= Math.floor(REVIEWS_STATS.average) ? '#fbbf24' : 'none'}
                    stroke="#fbbf24"
                  />
                ))}
              </div>
              <div className="rating-count">{REVIEWS_STATS.total.toLocaleString()} reviews</div>
            </div>
            <div className="rating-breakdown">
              {REVIEWS_STATS.breakdown.map((item) => (
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
              {POPULAR_KEYWORDS.map((keyword, index) => (
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