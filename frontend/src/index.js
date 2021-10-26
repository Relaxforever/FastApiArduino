import React from "react";
import { render } from 'react-dom';
import Header from "./components/Header";
import Charts from "./components/Charts";

function App() {
  return (
    <>
      <Header />
      <Charts />
    </>
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
