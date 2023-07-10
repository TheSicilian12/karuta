import React, { useEffect, useState } from "react";
import { useDispatch } from 'react-redux';

import "./LanguageToggle.css";

export default function LanguageToggle({languageOne, languageTwo}) {
  const [displayLanguage, setDisplayLanguage] = useState(languageOne)
  const [toggleCSS, setToggleCSS] = useState("language-toggle-toggle-off")

  if (!languageOne || !languageTwo) return null

  const toggle = () => {
    if (toggleCSS === "language-toggle-toggle-off") {
      setToggleCSS("language-toggle-toggle-on")
      setDisplayLanguage(languageTwo)
    } else {
      setToggleCSS("language-toggle-toggle-off")
      setDisplayLanguage(languageOne)
    }
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
