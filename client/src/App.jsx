// import './App.css'
import { Outlet } from 'react-router'
import Header from './Header'
import Footer from './Footer'
import { useState } from 'react';
import { Container } from 'react-bootstrap';

function App() {
  const [theme, setTheme] = useState(localStorage.getItem('theme'));
  return (
    <Container fluid data-bs-theme={theme}>
      <Header themeHandle={setTheme}/>
      <Outlet />
      <Footer />
    </Container>
  )
}

export default App
