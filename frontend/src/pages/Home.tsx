import { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";

function Home() {
  const { getAccessTokenSilently, user} = useAuth0();
  const [data, setData] = useState(null);
  const API_URL = import.meta.env.VITE_API_URL

  useEffect(() => {
    const fetchData = async () => {
        try{
            // JWT取得
            const token = await getAccessTokenSilently({
                authorizationParams: {
                    audience: "https://kss-api"
                }
            });
            console.log("JWT:", token);

            // API呼び出し
            const response = await fetch(`${API_URL}/init`, {
                headers: {
                Authorization: `Bearer ${token}`
                }
            });

            const json = await response.json();
            setData(json);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>ログインユーザー</h2>
      <pre>{JSON.stringify(user, null, 2)}</pre>

      <h2>APIレスポンス</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default Home;