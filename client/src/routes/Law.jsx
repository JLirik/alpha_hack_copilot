import SearchBar from "./components/SearchBar"
import { Card } from "react-bootstrap"

function Law() {
    const returnAnswer = () => {
        if (localStorage.getItem("answer") && localStorage.getItem("answer").answerType == 'law') {
            const answer = localStorage.getItem("answer").answer;
            return <Card><Card.Text>{answer}</Card.Text></Card>;
        }
    }
    return (
        <>
            <h1>Юриспруденция</h1>
            {returnAnswer()}
            <SearchBar apiEndpoint="query/law/explain" />
        </>)
}

export default Law