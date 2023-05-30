import './styles.css';

import * as React from 'react';
import {Link} from 'react-router-dom';
export const Login = () => {
  return (
    <div>
      <h1>Login page</h1>
      <Link to="/">Home</Link>
    </div>
  );
};

export default Login;
