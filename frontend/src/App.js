import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading....");

  useEffect(() => {
    const fetch_message = async () => {
      try {
        const data = await fetch("http://localhost:8000/api/hello/");
        setMessage(data.message);
      } catch (err) {
        console.log("An error has occurred:", err);
      }
    };
    fetch_message();
  }, []);
  return (
    <div style={{ padding: "6rem", fontFamily: "Arial", color: "black" }}>
      <h1>{message}</h1>
      <h1>{"This is an error"}</h1>
    </div>
  );
}

export default App;
