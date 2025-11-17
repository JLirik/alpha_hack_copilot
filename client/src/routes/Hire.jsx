import SearchBar from "./components/SearchBar"
import { Card } from "react-bootstrap";

function Hire() {
    const returnAnswer = () => {
        const stored = localStorage.getItem("answer");
        if (!stored) return null;

        let data;
        try {
            data = JSON.parse(stored);
        } catch {
            return null; 
        }

        if (data.answerType !== "hire") return null;

        const answer = data.answer;

        if (typeof answer === "object") {
            return Object.entries(answer).map(([key, item]) => (
                <Card key={key}><Card.Header>{item.answerType}</Card.Header><Card.Text>{item.answer}</Card.Text></Card>
            ));
        }

        return (
            <Card><Card.Header>{data.answerType}</Card.Header><Card.Text>{answer}</Card.Text></Card>
        );
    };

    return (
        <>
            <h1>Найм</h1>
            {returnAnswer()}
            <SearchBar apiEndpoint="query/hire" />
        </>)
}

export default Hire