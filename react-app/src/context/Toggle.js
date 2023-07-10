import React, { useRef, useState, useContext } from 'react';
import ReactDOM from 'react-dom';
// import './Modal.css';

const ToggleContext = React.createContext();

export function ToggleProvider({ children }) {
  const toggleRef = useRef();
  const [toggleContent, setToggleContent] = useState(null);
  // callback function that will be called when toggle is turned off (closing)
  const [onToggleOff, setOnToggleOff] = useState(null);

  const offToggle = () => {
    setToggleContent(null); // clear the toggle contents
    // If callback function is truthy, call the callback function and reset it
    // to null:
    if (typeof onToggleOff === 'function') {
      setOnToggleOff(null);
      onToggleOff();
    }
  };

  const contextValue = {
    toggleRef, // reference to modal div
    toggleContent, // React component to render inside toggle - not necessary, should adjust
    setToggleContent, // function to set the React component to render inside toggle
    setOnToggleOff, // function to set the callback function called when modal is turning off (closing)
    offToggle // function to turn toggle off (close the modal)
  };

  return (
    <>
      <ToggleContext.Provider value={contextValue}>
        {children}
      </ToggleContext.Provider>
      <div ref={modalRef} />
    </>
  );
}

export function Toggle() {
  const { toggleRef, toggleContent, offToggle } = useContext(ToggleContext);
  // If there is no div referenced by the modalRef or modalContent is not a
  // truthy value, render nothing:
  if (!toggleRef || !toggleRef.current || !toggleContent) return null;

  // Render the following component to the div referenced by the modalRef
  return ReactDOM.createPortal(
    <div id="toggle">
      <div id="toggle-background" onClick={toggleOff} />
      <div id="toggle-content">
        {toggleContent}
      </div>
    </div>,
    toggleRef.current
  );
}

export const useToggle = () => useContext(ToggleContext);
