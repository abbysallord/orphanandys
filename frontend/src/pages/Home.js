import React from 'react';
import Header from '../components/Header';
import Hero from '../components/Hero';
import About from '../components/About';
import MenuHighlights from '../components/MenuHighlights';
import Services from '../components/Services';
import Reviews from '../components/Reviews';
import BusyTimes from '../components/BusyTimes';
import Gallery from '../components/Gallery';
import Location from '../components/Location';
import Footer from '../components/Footer';

const Home = () => {
  return (
    <div>
      <Header />
      <Hero />
      <About />
      <MenuHighlights />
      <Services />
      <Reviews />
      <BusyTimes />
      <Gallery />
      <Location />
      <Footer />
    </div>
  );
};

export default Home;