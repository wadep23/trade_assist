import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    // TODO: Replace with actual auth API call
    navigate("/");
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    // TODO: Replace with actual auth API call
    // navigate("/dashboard");
    console.log("Register Pressed!");
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form
        onSubmit={handleRegister}
        className="bg-white p-8 rounded-xl shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl font-bold mb-6 text-center">
          Login to Trade Assist
        </h2>
        <input
          type="username"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full px-4 py-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full px-4 py-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full px-4 py-2 mb-6 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <button
          type="register"
          className="w-full bg-blue-600 text-white py-2 my-1 rounded hover:bg-blue-700 transition duration-200"
        >
          Register
        </button>
        <div className="flex content-center justify-center">
          <h2
            className="text-blue-600 cursor-pointer py-2 my-1 hover:text-green-600 transition duration-200"
            onClick={handleLogin}
          >
            Already registered? Login
          </h2>
        </div>
      </form>
    </div>
  );
};

export default Register;
