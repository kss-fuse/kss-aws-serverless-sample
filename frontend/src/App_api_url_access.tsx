import { useState } from "react"

function App() {

  const [message, setMessage] = useState("")

  const callApi = async () => {

    const response = await fetch(
      "https://nrl3tob9cl.execute-api.ap-northeast-1.amazonaws.com/dev/init"
    )

    const data = await response.json()

    setMessage(data.message)
  }

  return (
    <div>
      <h1>KSS Serverless Sample</h1>

      <button onClick={callApi}>
        API Call
      </button>

      <p>{message}</p>
    </div>
  )
}

export default App