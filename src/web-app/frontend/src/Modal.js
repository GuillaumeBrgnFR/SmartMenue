import React from "react";
import "./Modal.css";

function Modal({ isOpen, onClose, onSubmit }) {
  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const logo = formData.get("logo");
    const menu = formData.get("menu");

    // Créer une promesse pour chaque fichier uploadé
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

    try {
      // Attendez que toutes les promesses soient résolues
      const results = await Promise.all(promises);
      console.log("Résultats des uploads :", results);
      onSubmit(formData); // Passer les données au parent si nécessaire
      alert("Upload réussi !");
    } catch (error) {
      console.error("Erreur lors de l'upload :", error);
      alert("Erreur lors de l'upload, veuillez réessayer.");
    } finally {
      onClose(); // Fermer le modal
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
            <input type="file" id="logo" name="logo" accept="image/*" />
          </div>
          <div className="form-group">
            <label htmlFor="menu">Menu :</label>
            <input type="file" id="menu" name="menu" accept=".jpeg, .png, .jpg" />
          </div>
          <button type="submit" className="submit-button">Soumettre</button>
        </form>
      </div>
    </div>
  );
}

export default Modal;