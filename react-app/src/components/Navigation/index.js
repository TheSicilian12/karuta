import React, { useEffect, useState, useRef } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import ProfileButton from './ProfileButton';

import './Navigation.css';
import OpenModal from '../OpenModal';

function Navigation({ isLoaded }) {
	const dispatch = useDispatch()
	const history = useHistory()

	const [showMenu, setShowMenu] = useState(false);
	const ulRef = useRef();

	const openMenu = () => {
		if (showMenu) return;
		setShowMenu(true);
	};

	useEffect(() => {
		if (!showMenu) return;

		const closeMenu = (e) => {
			if (!ulRef.current.contains(e.target)) {
				setShowMenu(false);
			}
			// setShowMenu(false);
		};

		document.addEventListener("click", closeMenu);

		return () => document.removeEventListener("click", closeMenu);
	}, [showMenu]);

	const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

	const closeMenu = () => setShowMenu(false);

	const cartSideBar = () => {
		openMenu()
	}

	return (
		<div className="shinano-color-background nav-container">
			<div className="nav-prof-cart-container">
				<ul className={ulClassName} ref={ulRef}>
					<>
						<div>Hello</div>
					</>
				</ul>
			</div>
		</div>
	);
}

export default Navigation;
