import { useEffect, useState } from 'react'
import './App.css'
import { useLocation } from 'react-router';
import HistoryList from './routes/components/HistoryList';
import { Form, InputGroup, Button, CardGroup, Card } from 'react-bootstrap';
import { useNavigate } from 'react-router';
import fetcher from './routes/methods/Fetcher';
import { RegistrationError, AuthorizationError } from './routes/components/Errors';

function Footer() {
  const [history, setHistory] = useState(null);
  const [loading, setLoading] = useState(true);


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

  useEffect(() => {
    const loadHistory = async () => {
      try {
        const result = await fetcher("history/10", {}, "GET");
        setHistory(result);
        setLoading(false);
      } catch (e) {
        if ((e) == AuthorizationError) {
          
        }
      }
    }

    loadHistory();
  }, []);
  if (loading) return <p>Загрузка...</p>;
  return (
    <>
      <HistoryList data={history ? history : {}} />
    </>
  )
}

export default Footer
