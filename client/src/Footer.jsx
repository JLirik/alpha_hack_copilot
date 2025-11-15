import { useState } from 'react'
import './App.css'
import { useLocation } from 'react-router';
import { Form, InputGroup, Button, CardGroup, Card } from 'react-bootstrap';
import { useNavigate } from 'react-router';

function Footer() {
  let navigate = useNavigate();

  let location = useLocation();
  let topic = location.pathname.split('/') ? location.pathname.split('/').at(-1) : "";
  let apiAddress;
  switch (topic) {
    case "":
      apiAddress = 'general';
      break;
    case "marketing":
      apiAddress = "marketing/generate";
      break;
    case "law":
      apiAddress = "law/parse";
      break;
    case "hire":
      apiAddress = "hire/createOffer";
      break;
    case "finance":
      apiAddress = "finance";
      break;
  }

  return (
    <>
      <CardGroup></CardGroup>
    </>
  )
}

export default Footer
