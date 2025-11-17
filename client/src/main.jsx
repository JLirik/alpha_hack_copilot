import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import './index.css'
import 'bootstrap/dist/css/bootstrap.css';
import { BrowserRouter, Route, Routes } from 'react-router'
import App from './App.jsx'
import store from './routes/methods/store.js';
import { Provider } from 'react-redux';

import Login from './routes/Login.jsx'
import Home from './routes/Home.jsx'
import Register from './routes/Register.jsx'
import Settings from './routes/Settings.jsx'
import Marketing from './routes/Marketing.jsx'
import Hire from './routes/Hire.jsx'
import Law from './routes/Law.jsx';
import Finance from './routes/Finance.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>

    <BrowserRouter>
      <Routes>
        <Route path='/' element={<App />}>
          <Route index element={<Home />}></Route>
          <Route path='settings' element={<Settings />}></Route>
          <Route path='marketing' element={<Marketing />}></Route>
          <Route path='hire' element={<Hire />}></Route>
          <Route path='law' element={<Law />}></Route>
          <Route path='finance' element={<Finance />}></Route>
        </Route>
        <Route path='/login' element={<Login />}></Route>
        <Route path='/reg' element={<Register />}></Route>
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
