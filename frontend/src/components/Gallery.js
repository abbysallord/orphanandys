import React from 'react';
import { GALLERY_IMAGES } from '../data/mockData';
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from './ui/carousel';
import '../styles/Gallery.css';

const Gallery = () => {
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
            }}
            className="gallery-carousel"
          >
            <CarouselContent>
              {GALLERY_IMAGES.map((image, index) => (
                <CarouselItem key={index} className="md:basis-1/2 lg:basis-1/3">
                  <div className="gallery-item">
                    <img src={image.url} alt={image.alt} />
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