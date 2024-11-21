// App.js
import React, { useState, useEffect, useRef } from "react";
import "./App.css";
import Menu from "./Menu";
import Modal from "./Modal";
import { FaSave, FaPencilAlt } from "react-icons/fa";


function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [menuTitle, setMenuTitle] = useState("Menu");
  const [isEditMode, setIsEditMode] = useState(false);
  const menuRef = useRef(null); // Référence vers le composant Menu

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

    const handleSave = () => {
    if (menuRef.current) {
      const categories = menuRef.current.getCategories();

      // Envoyer les données au backend
      fetch('/api/save-menu', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(categories),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Erreur lors de la sauvegarde du menu');
          }
          return response.json();
        })
        .then((data) => {
          console.log('Menu sauvegardé avec succès');
          // Recharger la page
          window.location.reload();
        })
        .catch((error) => {
          console.error('Erreur :', error);
          alert('Une erreur est survenue lors de la sauvegarde du menu');
        });
    }
  };

  // Fonction pour basculer le mode édition
  const toggleEditMode = () => {
    if (isEditMode) {
      // Si on quitte le mode édition, on sauvegarde les modifications
      handleSave();
    }
    setIsEditMode((prevMode) => !prevMode);
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
                <div className="header-buttons">
                    <button className="custom-button" onClick={openModal}>
                        Importer un menu
                    </button>
                </div>
            </header>
            <div className="container">
                <Menu ref={menuRef} isEditMode={isEditMode}/>
            </div>
            <button
                className={`custom-edit-button ${isEditMode ? "save-mode" : "edit-mode"}`}
                onClick={toggleEditMode}
            >
                {isEditMode ? (
                    <>
                        <FaSave style={{marginRight: "8px"}}/> Sauvegarder
                    </>
                ) : (
                    <>
                        <FaPencilAlt style={{marginRight: "8px"}}/> Édition
                    </>
                )}
            </button>
            <Modal isOpen={isModalOpen} onClose={closeModal} onSubmit={handleSubmit}/>
        </div>
    );
}

export default App;