import { CardGroup, Card } from 'react-bootstrap';
import { Link } from 'react-router';
import SearchBar from './components/SearchBar';

function Home() {
    const returnAnswer = () => {
        if (localStorage.getItem("answer")) {
            localStorage.removeItem("answer");
            return <Card><Card.Text>{localStorage.getItem("answer").answer}</Card.Text></Card>;
        }
    }
    return (
        <>
            <CardGroup>
                <Card className='front-choice'>
                    <Link to={"/marketing"}>
                        <Card.Title>Маркетинг</Card.Title>
                        <Card.Text>Расскажи о своем бизнесе миру!</Card.Text>
                    </Link>

                </Card>
                <Card className='front-choice'>
                    <Link to={"/hire"}>
                        <Card.Title>Найм</Card.Title>
                        <Card.Text>Найди преданных единомышленников!</Card.Text>
                    </Link>
                </Card>

                <Card className='front-choice'>
                    <Link to={"/law"}>
                        <Card.Title>Юриспруденция</Card.Title>
                        <Card.Text>Защитись от правовых проблем!</Card.Text>
                    </Link>
                </Card>

                <Card className='front-choice'>
                    <Link to={"/finance"}>
                        <Card.Title>Финансы</Card.Title>
                        <Card.Text>Рассчитай деньги для своих идей!</Card.Text>
                    </Link>
                </Card>
            </CardGroup >
            {returnAnswer()}
            <SearchBar apiEndpoint="general"/>
        </>
    )
}

export default Home