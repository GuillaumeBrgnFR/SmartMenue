import React, { useState, useEffect } from "react";
import "./App.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronDown, faChevronRight } from "@fortawesome/free-solid-svg-icons";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import Modal from "./Modal";



function Menu() {
  const [categories, setCategories] = useState([]);
  const [activeIndex, setActiveIndex] = useState(null);

  useEffect(() => {
    fetch('/api/menu')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Erreur HTTP ! statut : ${response.status}`);
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
    setActiveIndex(index === activeIndex ? null : index);
  };

  return (
    <div className="menu-container">
      {categories.map((category, index) => (
        <MenuSection
          key={index}
          title={category.category_name}
          items={category.category_items}
          prices={category.item_prices}
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


function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [menuTitle, setMenuTitle] = useState("Menu");

  useEffect(() => {
    fetch("/api/get-menu-name")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Erreur lors de la récupération du nom du menu");
        }
        return response.json();
      })
      .then((data) => {
        if (data.menuName) {
          setMenuTitle(data.menuName);
        }
      })
      .catch((error) => {
        console.error("Erreur :", error);
      });
  }, []);

  const openModal = () => setIsModalOpen(true);
  const closeModal = () => {
    setIsModalOpen(false);
    window.location.reload();
  };

  const handleSubmit = (formData) => {
    const menuName = formData.get("menuName");
    if (menuName) setMenuTitle(menuName);
    closeModal();
  };

  return (
    <div className="App">
      <header className="App-header">
        <img
          src="/images/logos/logo.png"
          alt="Logo"
          className="restaurant-logo"
        />
        <h1 className="page-title">{menuTitle}</h1>
        <button className="custom-button" onClick={openModal}>
          Importer un menu
        </button>
      </header>
      <div className="container">
        <Menu />
      </div>
      <Modal isOpen={isModalOpen} onClose={closeModal} onSubmit={handleSubmit} />
    </div>
  );
}

export default App;