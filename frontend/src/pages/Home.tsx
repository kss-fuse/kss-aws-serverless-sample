import { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";

function Home() {
  const { getAccessTokenSilently } = useAuth0();
  const [data, setData] = useState(null);
  const API_URL = import.meta.env.VITE_API_URL

  useEffect(() => {
    const fetchData = async () => {
      const token = await getAccessTokenSilently();
      const response = await fetch(`${API_URL}init`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      const json = await response.json();
      setData(json);
    };

    fetchData();
  }, []);

  return <div>{JSON.stringify(data)}</div>;
}

export default Home;