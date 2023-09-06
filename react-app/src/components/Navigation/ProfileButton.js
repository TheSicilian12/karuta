import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { logout } from "../../store/session";
import { useSelector } from "react-redux";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const history = useHistory();
  const sessionUser = useSelector(state => state.session.user);
  let userCheck = false;
  if (user !== null) userCheck = true;

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      // if (!ulRef.current.contains(e.target)) {
      //   setShowMenu(false);
      // }
      setShowMenu(false);
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push("/")
    closeMenu()
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <ul className={`${ulClassName} nav-bar-profile-dropdown nav-bar-font`} ref={ulRef}>
        {user ? (
          <div className="nav-bar-user-dropdown">
            <div className="nav-bar-dropwdown-margin">{user.username}</div>
              <div className="nav-bar-dropwdown-margin">{user.email}</div>
              <button className="nav-bar-dropwdown-margin button-full" onClick={handleLogout}>Log Out</button>
          </div>
        ) : (
          <div className="nav-bar-logged-out-dropdown">
            {/* <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            /> */}
            <div className="nav-profile-button-container">
              <i className="fa fa-user"></i>
            </div>

            <button
                className="nav-bar-dropwdown-margin button-full"
                onClick={() => {
                history.push("/login")
                closeMenu()
              }}>
              Log In
            </button>

            {/* <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            /> */}
            <button
              className="nav-bar-dropwdown-margin button-full"
              onClick={() => {
                history.push("/signup")
                closeMenu()
              }}>
              Sign Up
            </button>
          </div>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
