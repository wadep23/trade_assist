import React, {useState} from 'react'
import { useNavigate } from "react-router-dom";

import UserIcon from "../icons/UserIcon";
import { AuthServiceProvider } from "../services/AuthServiceProvider";
import Logo from '../icons/Logo';

export default function Header() {
    const navigate = useNavigate();
    const [error, setError] = useState(null);

    const handleLogout = async (e) => {
    e.preventDefault();

    const authService = new AuthServiceProvider("/api/graphql/");
    try {
      await authService.logout();
      navigate("/");
    } catch (error) {
      setError(error.message);
    }
    console.log("Logout pressed");
  };
    
  return (
    <div className="flex justify-between items-center px-5 py-3">
        {/* <Logo /> */}
      <h1 className="text-2xl cursor-pointer text-green-500 font-semibold" onClick={() => console.log("Home clicked")}>
        Trade Assist
      </h1>
      <div className="flex items-center space-x-4">
        <div
          className="cursor-pointer p-1"
          onClick={() => console.log("Profile clicked!")}
        >
          <UserIcon />
        </div>
        <h2
          className="text-lg cursor-pointer text-green-500"
          onClick={handleLogout}
        >
          logout
        </h2>
      </div>
    </div>
  )
}
