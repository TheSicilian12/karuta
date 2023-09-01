import React, { useEffect, useState, useRef } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import ProfileButton from './ProfileButton';

import './Navigation.css';
// import OpenModal from '../OpenModal';

function Navigation({ isLoaded }) {
	const ulRef = useRef();
	const history = useHistory();

	const [showMenu, setShowMenu] = useState(false);

	const sessionUser = useSelector(state => state.session.user);

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
		};

		document.addEventListener("click", closeMenu);

		return () => document.removeEventListener("click", closeMenu);
	}, [showMenu]);

	const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

	const closeMenu = () => setShowMenu(false);

	const cartSideBar = () => {
		openMenu()
	}

	const redirectPoems = () => {
		history.push('/100poems')
	}

	const redirectHomepage = () => {
		history.push('/')
	}

	const redirectPoemPractice = () => {
		history.push('/poempractice')
	}

	const redirectStudyDeck = () => {
		history.push('/studyDecks')
	}

	return (
		<div className="nav-bar-container">
			<div
				onClick={() => redirectPoems()}
				className="nav-bar-links"
			>
				Poems
			</div>

			<button
				onClick={() => redirectPoemPractice()}
			>
				Poem Practice
			</button>
			<button
				onClick={() => redirectStudyDeck()}
			>
				Study Decks
			</button>
			{isLoaded &&
				<ProfileButton user={sessionUser} />
			}
		</div>
	);
}

export default Navigation;
