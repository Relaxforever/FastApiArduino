import React from "react";
import { render } from 'react-dom';
import Header from "./components/Header";
import Charts from "./components/Charts";
import "./index.css"

function App() {
  return (
    <>
      <div className="m-header">
        <Header />
      </div>
      <div className="m-body">
        <Charts />
      </div>

    </>
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
