import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import "./LoginForm.css";

function LoginFormPage() {
  const dispatch = useDispatch();
  const history = useHistory();
  const sessionUser = useSelector((state) => state.session.user);

  const [errors, setErrors] = useState({})
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  return (
    <div>Login Form Page
      <form
        onSubmit={handleSubmit}
      >

        {/* Email */}
        <div>
          <label>
            Email
          </label>
          <input
            type="text"
            value={email}
            onChange={(e) => {
              setEmail(e.target.value)
              // setDisEmailErr(true)
            }}
          // required
          />
        </div>

        {/* Password */}
        <div>
          <label>
            Password
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value)
              // setDisPassErr(true)
            }}
          // required
          />
        </div>

        <button
          type="submit"
          // disabled={Object.values(err).length > 0}
          >
          Log In
        </button>

      </form>
    </div>
  );
}

export default LoginFormPage;
