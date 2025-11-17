import SearchBar from "./components/SearchBar"
function Hire() {
    const returnAnswer = () => {
        if (localStorage.getItem("answer") && localStorage.getItem("answer").answerType == 'law') {
            const answer = localStorage.getItem("answer").answer;
            return <Card><Card.Text>{answer}</Card.Text></Card>;
        }
    }
    return (
        <>
            <h1>Найм</h1>
            {returnAnswer()}
            <SearchBar apiEndpoint="query/law/explain" />
        </>)
}

export default Hire