import React, { useState } from "react";
import "./Modal.css";

function Modal({ isOpen, onClose, onSubmit }) {
  const [isLoading, setIsLoading] = useState(false); // État pour le chargement

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true); // Commence le chargement

    const formData = new FormData(e.target);

    const logo = formData.get("logo");
    const menu = formData.get("menu");
    const menuName = formData.get("menuName");

    const promises = [];

    if (logo && logo.size > 0) {
      const logoFormData = new FormData();
      logoFormData.append("logo", logo);

      promises.push(
        fetch("/api/upload-logo", {
          method: "POST",
          body: logoFormData,
        }).then((response) => {
          if (!response.ok) {
            throw new Error("Erreur lors de l'upload du logo");
          }
          return response.json();
        })
      );
    }

    if (menu && menu.size > 0) {
      const menuFormData = new FormData();
      menuFormData.append("menu", menu);

      promises.push(
        fetch("/api/upload-menu", {
          method: "POST",
          body: menuFormData,
        }).then((response) => {
          if (!response.ok) {
            throw new Error("Erreur lors de l'upload du menu");
          }
          return response.json();
        })
      );
    }

    if (menuName && menuName.trim() !== "") {
      promises.push(
        fetch("/api/save-menu-name", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ menuName: menuName }),
        }).then((response) => {
          if (!response.ok) {
            throw new Error("Erreur lors de la sauvegarde du nom du menu");
          }
          return response.json();
        })
      );
    }

    try {
      const results = await Promise.all(promises);
      console.log("Résultats des uploads :", results);
      onSubmit(formData);
      alert("Upload réussi !");
    } catch (error) {
      console.error("Erreur lors de l'upload :", error);
      alert("Erreur lors de l'upload, veuillez réessayer.");
    } finally {
      setIsLoading(false); // Arrête le chargement
      onClose(); // Ferme le modal
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="modal-close" onClick={onClose}>
          X
        </button>
        <h2>Importer un menu</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="menuName">Nom du restaurant :</label>
            <input type="text" id="menuName" name="menuName" />
          </div>
          <div className="form-group">
            <label htmlFor="logo">Logo :</label>
            <input type="file" id="logo" name="logo" accept=".png" />
          </div>
          <div className="form-group">
            <label htmlFor="menu">Menu :</label>
            <input type="file" id="menu" name="menu" accept=".jpeg, .png, .jpg" />
          </div>
          <button type="submit" className="submit-button" disabled={isLoading}>
            {isLoading ? "Chargement..." : "Soumettre"}
          </button>
        </form>
        {isLoading && (
          <div className="loading-container">
            <div className="spinner"></div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Modal;