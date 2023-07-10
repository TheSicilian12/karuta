import React, { useState } from "react";

import "./LanguageToggle.css";

export default function LanguageToggle({displayLanguage, setDisplayLanguage, languageOne, languageTwo}) {
  // Language toggle takes in:
  // 1. const [displayLanguage, setDisplayLanguage] = useState("")
  //    - displayLanguage
  //    - setDisplayLanguage
  // 2. languageOne, default language
  // 3. languageTwo, optional language

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
