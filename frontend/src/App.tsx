import axios from "axios";
import { useAuth0 } from "@auth0/auth0-react";
import Home from "./pages/Home";

axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.headers.post["access-control-allow-origin"] = "*";

function App() {
 
  const { loginWithRedirect, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      <h1>KSS Serverless Sample</h1>

      {!isAuthenticated ? (
        <button onClick={() => loginWithRedirect()}>
          ログイン
        </button>
      ) : (
        <Home />
      )}
    </div>
  );

}

export default App