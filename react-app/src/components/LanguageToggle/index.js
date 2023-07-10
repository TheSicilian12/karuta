import React, { useEffect } from "react";
import { useDispatch } from 'react-redux';

import "./LanguageToggle.css";

export default function LanguageToggle(languageOne, languageTwo) {
  console.log("test")

  if (!languageOne || !languageTwo) return null

  let toggleCSS = ""
  const toggle = () => {
    toggleCSS = "langauge-toggle-start-toggle"
    console.log(toggleCSS)
  }

  return (
    <div className={`language-toggle-container`}>
      <div
        className="language-toggle-item"
        onClick={() => toggle()}
        >

      </div>
    </div>
  );
}
