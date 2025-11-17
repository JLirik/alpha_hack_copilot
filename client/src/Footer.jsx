import { useEffect, useState } from 'react'
import './App.css'
import { data, useLocation } from 'react-router';
import HistoryList from './routes/components/HistoryList';
import { Form, InputGroup, Button, CardGroup, Card } from 'react-bootstrap';
import { useNavigate } from 'react-router';

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
      const result = await fetcher("history/10", {}, "GET");
      setHistory(result);
      setLoading(false);
    }

    loadHistory();
  }, []);
  return (
    <>
      <HistoryList data={history ? history : {}}/>
    </>
  )
}

export default Footer
