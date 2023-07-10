import React, { useEffect, useState } from "react";
import { useDispatch } from 'react-redux';

import "./LanguageToggle.css";

export default function LanguageToggle(languageOne, languageTwo) {
  const [displayLanguage, setDisplayLanguage] = useState(languageOne)
  const [toggleCSS, setToggleCSS] = useState("")

  if (!languageOne || !languageTwo) return null

  const toggle = () => {
    if (toggleCSS === "language-toggle-toggle-on") {
      setToggleCSS("language-toggle-toggle-off")
    } else setToggleCSS("language-toggle-toggle-on")

  }

  return (
    <div className={`language-toggle-container ${toggleCSS}`}>
      <div
        className="language-toggle-item"
        onClick={() => toggle()}
        >

      </div>
    </div>
  );
}
