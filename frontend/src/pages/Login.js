import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthServiceProvider } from "../services/AuthServiceProvider";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e, email, password) => {
    e.preventDefault();
    // TODO: Replace with actual auth API call
    const authService = new AuthServiceProvider("/api/graphql/");

    try {
      await authService.login(email, password);
      const user = await authService.me();
      console.log("Logged in as:", user.username);
    } catch (err) {
      console.error(err.message);
    }
    navigate("/dashboard");
    console.log("Login pressed!");
  };

  const handleRegister = (e) => {
    e.preventDefault();
    navigate("/register");
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form
        onSubmit={handleLogin}
        className="bg-white p-8 rounded-xl shadow-md w-full max-w-sm"
      >
        <h2 className="text-2xl font-bold mb-6 text-center">
          Login to Trade Assist
        </h2>
        <input
          type="text"
          placeholder="Email or Username"
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
          type="submit"
          className="w-full bg-blue-600 text-white py-2 my-1 rounded hover:bg-blue-700 transition duration-200"
        >
          Login
        </button>
        <div className="flex content-center justify-center">
          <h1
            type="register"
            onClick={handleRegister}
            className="text-blue-600 cursor-pointer py-2 my-1 rounded hover:text-green-600 transition duration-200"
          >
            Register
          </h1>
        </div>
      </form>
    </div>
  );
};

export default Login;
