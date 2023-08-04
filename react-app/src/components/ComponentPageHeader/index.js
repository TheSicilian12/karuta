import React, { useEffect, useState, useRef } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

import './ComponentPageHeader.css';
// import OpenModal from '../OpenModal';

function ComponentPageHeader({ title, subTitle }) {
	const ulRef = useRef();
	const history = useHistory();

	return (
		<div>
			<div>
				{title}
			</div>
			<div>
				{subTitle}
			</div>
		</div>
	);
}

export default ComponentPageHeader;
