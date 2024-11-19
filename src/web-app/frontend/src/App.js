import React, { useState, useEffect } from "react";
import "./App.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronDown, faChevronRight } from "@fortawesome/free-solid-svg-icons";
import { faUpload } from "@fortawesome/free-solid-svg-icons";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="page-title">Menu</h1>
        <button className="custom-button">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="currentColor"
            width="16px"
            height="16px"
            style={{ marginRight: "10px" }}
          >
            <path d="M4 4v2h16V4H4zm6 7.59V20h4v-8.41l2.29 2.29 1.42-1.42L12 8l-5.71 5.71 1.42 1.42L10 11.59z" />
          </svg>
          Importer un menu
        </button>
      </header>
      <Menu />
    </div>
  );
}

function Menu() {
  const [categories, setCategories] = useState([]); // État pour stocker les catégories
  const [activeIndex, setActiveIndex] = useState(null); // État pour gérer l'index actif

  // Récupérer les catégories depuis l'API Flask
  useEffect(() => {
  fetch('/api/menu')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (!data || !data.categories || data.categories.length === 0) {
        throw new Error("Données JSON invalides !");
      }
      setCategories(data.categories);
    })
    .catch((error) => {
      console.error('Erreur lors de la récupération des catégories :', error);
    });
}, []);

  const toggleVisibility = (index) => {
    setActiveIndex(index === activeIndex ? null : index); // Alterner l'état d'affichage
  };

  return (
    <div className="menu-container">
      {categories.map((category, index) => (
        <MenuSection
            key={index}
            title={category.category_name}
            items={category.category_items}
            prices={category.category_prices}
            isVisible={index === activeIndex}
            onClick={() => toggleVisibility(index)}
        />
      ))}
    </div>
  );
}

function MenuSection({ title, items = [], prices = [], isVisible, onClick }) {
  return (
    <div className="category">
      <h2 onClick={onClick} className="category-header">
        <span className="category-title">{title}</span>
        <span className={`arrow ${isVisible ? "down" : "right"}`}>▼</span>
      </h2>
      <ul className={isVisible ? "visible" : ""}>
        {items.map((item, index) => (
          <li key={index}>
            <span className="item-name">{item}</span>
            <span className="item-price">{prices[index]}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;