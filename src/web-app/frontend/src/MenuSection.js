// MenuSection.js
import React from "react";
import { FaTrash, FaPlus } from "react-icons/fa";
import "./App.css";

function MenuSection({ index, category, isVisible, onToggle, isEditMode, updateCategory, deleteCategory }) {
  // Fonction pour mettre à jour le nom de la section
  const handleCategoryNameChange = (e) => {
    const updatedCategory = { ...category, category_name: e.target.value };
    updateCategory(index, updatedCategory);
  };

  const handleDeleteClick = (e) => {
    e.stopPropagation(); // Empêche le déroulement de la section
    deleteCategory(index);
  };

  // Fonction pour mettre à jour un item
  const handleItemChange = (itemIndex, field, value) => {
    const updatedItems = [...category.category_items];
    const updatedPrices = [...category.item_prices];

    if (field === 'name') {
      updatedItems[itemIndex] = value;
    } else if (field === 'price') {
      updatedPrices[itemIndex] = value;
    }

    const updatedCategory = {
      ...category,
      category_items: updatedItems,
      item_prices: updatedPrices,
    };

    updateCategory(index, updatedCategory);
  };

  const deleteItem = (itemIndex) => {
    const updatedItems = category.category_items.filter((_, i) => i !== itemIndex);
    const updatedPrices = category.item_prices.filter((_, i) => i !== itemIndex);

    const updatedCategory = {
      ...category,
      category_items: updatedItems,
      item_prices: updatedPrices,
    };

    updateCategory(index, updatedCategory);
  };

  // Fonction pour ajouter un nouvel item
  const addItem = () => {
    const updatedItems = [...category.category_items, ""];
    const updatedPrices = [...category.item_prices, ""];
    const updatedCategory = {
      ...category,
      category_items: updatedItems,
      item_prices: updatedPrices,
    };
    updateCategory(index, updatedCategory);
  };

  // Empêcher la propagation du clic sur l'input du titre en mode édition
  const handleTitleClick = (e) => {
    e.stopPropagation();
  };

  return (
    <div className="category">
      <div className="category-header" onClick={() => onToggle(index)}>
        {isEditMode ? (
            <>
              {/* Icône de suppression à gauche */}
              <button className="delete-button" onClick={handleDeleteClick}>
                <FaTrash/>
              </button>
              <input
                  type="text"
                  value={category.category_name}
                  onChange={handleCategoryNameChange}
                  className="category-title-input"
                  onClick={handleTitleClick}
              />
            </>
        ) : (
            <>
              <span className="category-title">{category.category_name}</span>
            </>
        )}
        {/* Flèche pour dérouler/replier la section */}
        <span className={`arrow ${isVisible ? 'down' : 'right'}`}>▼</span>
      </div>
      {isVisible && (
          <ul className={isVisible ? 'visible' : 'hidden'}>
          {category.category_items.map((item, itemIndex) => (
            <li key={itemIndex}>
              {isEditMode ? (
                <>
                  <input
                    type="text"
                    value={item}
                    onChange={(e) => handleItemChange(itemIndex, 'name', e.target.value)}
                    className="item-name-input"
                    onClick={(e) => e.stopPropagation()}
                  />
                  <input
                    type="text"
                    value={category.item_prices[itemIndex]}
                    onChange={(e) => handleItemChange(itemIndex, 'price', e.target.value)}
                    className="item-price-input"
                    onClick={(e) => e.stopPropagation()}
                  />
                  {/* Icône de suppression pour le plat */}
                  <button
                    className="delete-button"
                    onClick={(e) => {
                      e.stopPropagation();
                      deleteItem(itemIndex);
                    }}
                  >
                    <FaTrash />
                  </button>
                </>
              ) : (
                <>
                  <span className="item-name">{item}</span>
                  <span className="item-price">{category.item_prices[itemIndex]}</span>
                </>
              )}
            </li>
          ))}
          {/* Ligne pour ajouter un nouveau plat en mode édition */}
          {isEditMode && (
            <li>
              <input
                type="text"
                value=""
                onChange={(e) => handleItemChange(category.category_items.length, 'name', e.target.value)}
                className="item-name-input"
                onClick={(e) => e.stopPropagation()}
                placeholder="Nouveau plat"
              />
              <input
                type="text"
                value=""
                onChange={(e) => handleItemChange(category.item_prices.length, 'price', e.target.value)}
                className="item-price-input"
                onClick={(e) => e.stopPropagation()}
                placeholder="Prix"
              />
              {/* Bouton pour ajouter le plat */}
              <button
                className="add-item-button"
                onClick={(e) => {
                  e.stopPropagation();
                  addItem();
                }}
              >
                <FaPlus />
              </button>
            </li>
          )}
        </ul>
      )}
    </div>
  );
}

export default MenuSection;