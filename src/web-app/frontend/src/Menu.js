// Menu.js
import React, { useState, useEffect, useImperativeHandle, forwardRef } from "react";
import MenuSection from "./MenuSection";
import { FaPlus } from "react-icons/fa";
import "./App.css"

const Menu = forwardRef(({ isEditMode }, ref) => {
  const [categories, setCategories] = useState([]);
  const [activeIndex, setActiveIndex] = useState(null);

  useEffect(() => {
    fetch('/api/menu')
      .then((response) => response.json())
      .then((data) => {
        setCategories(data.categories || []);
      })
      .catch((error) => {
        console.error('Erreur lors de la récupération des catégories :', error);
      });
  }, []);

const toggleVisibility = (index) => {
  console.log(`Toggling visibility for index: ${index}`);
  setActiveIndex(prevIndex => (prevIndex === index ? null : index));
  console.log('New activeIndex:', activeIndex);
};

useEffect(() => {
  console.log('activeIndex changed to:', activeIndex);
}, [activeIndex]);

  const updateCategory = (index, updatedCategory) => {
    const newCategories = [...categories];
    newCategories[index] = updatedCategory;
    setCategories(newCategories);
  };

  const deleteCategory = (index) => {
    const newCategories = categories.filter((_, i) => i !== index);
    setCategories(newCategories);
  };

  // Exposer les données du menu au composant parent via une référence
  useImperativeHandle(ref, () => ({
    getCategories: () => categories,
  }));

  const addCategory = () => {
    const newCategory = {
      category_name: "Nouvelle catégorie",
      category_items: [],
      item_prices: [],
    };
    setCategories([...categories, newCategory]);
  };

  return (
    <div className="menu-container">
      {categories.map((category, index) => (
        <MenuSection
          key={index}
          index={index}
          category={category}
          isVisible={activeIndex === index}
          onToggle={toggleVisibility}
          isEditMode={isEditMode}
          updateCategory={updateCategory}
          deleteCategory={deleteCategory}
        />
      ))}
      {isEditMode && (
        <button className="add-category-button" onClick={addCategory}>
          <FaPlus /> Ajouter une catégorie
        </button>
      )}
    </div>
  );
});

export default Menu;