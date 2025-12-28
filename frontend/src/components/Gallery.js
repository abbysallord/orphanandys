import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from './ui/carousel';
import '../styles/Gallery.css';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const Gallery = () => {
  const [galleryImages, setGalleryImages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchGalleryImages = async () => {
      try {
        const response = await axios.get(`${API}/gallery`);
        setGalleryImages(response.data);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching gallery images:', err);
        setLoading(false);
      }
    };

    fetchGalleryImages();
  }, []);

  if (loading || galleryImages.length === 0) {
    return (
      <section id="gallery" className="section gallery-section">
        <div className="container">
          <div className="section-header">
            <h2>Experience Orphan Andy's</h2>
            <p>Loading gallery...</p>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="gallery" className="section gallery-section">
      <div className="container">
        <div className="section-header">
          <h2>Experience Orphan Andy's</h2>
          <p>A glimpse into our diner and delicious offerings</p>
        </div>
        <div className="gallery-carousel-wrapper">
          <Carousel 
            opts={{
              align: 'start',
              loop: true,
              skipSnaps: false,
              dragFree: false,
            }}
            className="gallery-carousel"
          >
            <CarouselContent className="-ml-4">
              {galleryImages.map((image, index) => (
                <CarouselItem key={image._id || index} className="pl-4 md:basis-1/2 lg:basis-1/3">
                  <div className="gallery-item">
                    <img src={image.url} alt={image.alt} loading="lazy" />
                  </div>
                </CarouselItem>
              ))}
            </CarouselContent>
            <CarouselPrevious className="carousel-btn" />
            <CarouselNext className="carousel-btn" />
          </Carousel>
        </div>
      </div>
    </section>
  );
};

export default Gallery;