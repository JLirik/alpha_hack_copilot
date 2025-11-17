import { Form, InputGroup, Button, CardGroup, Card } from 'react-bootstrap';
import { useNavigate } from 'react-router';
import fetcher from '../methods/Fetcher';


function SearchBar(apiEndpoint) {
  let navigate = useNavigate();

  const sendQuery = (formData) => {
    if (!formData.get("question")) return;
    const accessToken = "MYTOKEN";
    fetcher(apiEndpoint, accessToken, { "query": formData.get("question") }).catch((e) => navigate("/reg")).then(data => {
        if (data) {
          localStorage.setItem("answer", data);
          navigate(data.answerType != "other" ? "/" + data.answerType : "/");
        } else localStorage.setItem("answer", "Не получилось сгенерировать ответ");
      });
  }

  return (
    <>
      <Form action={sendQuery}>
        <InputGroup className="mb-3">
          <Form.Control
            placeholder="Готов ответить на твой вопрос..."
            aria-label="Готов ответить на твой вопрос..."
            name="question"
            as={'textarea'}
            rows={2}
          />
          <Button variant="outline-primary" type='submit'>
            <i className="bi bi-send"></i>
          </Button>
        </InputGroup>
      </Form>
    </>
  )
}

export default SearchBar
