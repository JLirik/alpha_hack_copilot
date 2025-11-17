import SearchBar from "./components/SearchBar"
import { Card } from "react-bootstrap";
function Hire() {
    const returnAnswer = () => {
        if (localStorage.getItem("answer") && localStorage.getItem("answer").answerType == 'hire') {
            const answer = localStorage.getItem("answer").answer;
            return <Card><Card.Text>{answer}</Card.Text></Card>;
        }
    }
    return (
        <>
            <h1>Найм</h1>
            {returnAnswer()}
            <SearchBar apiEndpoint="query/hire" />
        </>)
}

export default Hire