import { Form, InputGroup, Button, CardGroup, Card } from 'react-bootstrap';
import { useNavigate } from 'react-router';
import fetcher from '../methods/Fetcher';


function SearchBar({ apiEndpoint }) {
  let navigate = useNavigate();

  const sendQuery = (formData) => {
    const question = formData.get("question");
    if (!question) return;

    fetcher(apiEndpoint, { query: question })
      .catch(() => navigate("/reg"))
      .then(data => {
        if (!data) {
          const fallback = {
            answerType: "other",
            answer: "Не получилось сгенерировать ответ",
          };
          localStorage.setItem("answer", JSON.stringify(fallback));
          return;
        }

        localStorage.setItem("answer", JSON.stringify(data));

        navigate(data.answerType !== "other" ? `/${data.answerType}` : "/");
      });
  };

  return (
    <Form action={sendQuery}>
      <InputGroup className="mb-3">
        <Form.Control
          placeholder="Готов ответить на твой вопрос..."
          name="question"
          as="textarea"
          rows={2}
        />
        <Button variant="outline-primary" type="submit">
          <i className="bi bi-send"></i>
        </Button>
      </InputGroup>
    </Form>
  );
}

export default SearchBar;
