import SearchBar from "./components/SearchBar"
import LatexRenderer from "./methods/LatexRenderer"
import { LatexExample } from "./methods/LatexExample"
import { Card } from "react-bootstrap"

function Finance() {
    const returnAnswer = () => {
        if (localStorage.getItem("answer") && localStorage.getItem("answer").answerType == 'finance') {
            const answer = localStorage.getItem("answer").answer;
            return <Card><Card.Text><LatexRenderer content={answer}/></Card.Text></Card>;
        }
    }
    return (
    <>
    <h1>Финансы</h1>
    <Card><Card.Text><LatexRenderer content={LatexExample}/></Card.Text></Card>
    {returnAnswer()}
    <SearchBar apiEndpoint="query/finance"/>
    </>
    )
}

export default Finance