import React from "react";
import "./Modal.css";

function Modal({ isOpen, onClose, onSubmit }) {
  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    onSubmit(formData); // Passer les données au parent
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="modal-close" onClick={onClose}>X</button>
        <h2>Importer un menu</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="menuName">Nom du restaurant :</label>
            <input type="text" id="menuName" name="menuName"/>
          </div>
          <div className="form-group">
            <label htmlFor="logo">Logo :</label>
            <input type="file" id="logo" name="logo" accept="image/*"/>
          </div>
          <div className="form-group">
            <label htmlFor="menu">Menu :</label>
            <input type="file" id="menu" name="menu" accept="image/*"/>
          </div>
          <button type="submit" className="submit-button">Soumettre</button>
        </form>
      </div>
    </div>
  );
}

export default Modal;