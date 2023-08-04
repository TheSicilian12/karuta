import React, { useEffect, useState, useRef } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

import './ComponentPageHeader.css';
// import OpenModal from '../OpenModal';

function ComponentPageHeader({ title, image }) {
	const ulRef = useRef();
	const history = useHistory();

	return (
		<div className="component-page-header-container">
			<img src={image}
			className="component-page-background-image" />
			<div className="component-page-header-title">
				{title}
			</div>
		</div>
	);
}

export default ComponentPageHeader;
