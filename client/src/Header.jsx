import './App.css'
import { Col, Container, Form, Nav, Navbar, NavDropdown, Row, Button, ToggleButton } from 'react-bootstrap';

function Header({ themeHandle }) {
    const handleChange = (event) => {
        localStorage.setItem('theme', event.target.checked ? "dark" : "light");
        document.querySelector("body").setAttribute("data-bs-theme", event.target.checked ? "dark" : "light");
        themeHandle(event.target.checked ? "dark" : "light");
    };

    var nowHours = new Date().getHours();
    var greeting;
    if (5 <= nowHours && nowHours <= 11) {
        greeting = "Доброе утро";
    } else if (12 <= nowHours && nowHours <= 16) {
        greeting = "Добрый день";
    } else if (17 <= nowHours && nowHours <= 21) {
        greeting = "Добрый вечер";
    } else {
        greeting = "Доброй ночи";
    }
    var last_part = "";
    if (localStorage.getItem("name")) {
        last_part = `, ${localStorage.getItem("name")}`;
    }
    last_part += "!";
    return (
        <>
            <Navbar expand="lg" className="bg-body-tertiary">
                <Container>
                    <Navbar.Brand href="/">
                        <img
                            alt="Логотип Альфа-банка"
                            src="././image.png"
                            width="30"
                            height="30"
                            className="d-inline-block align-center"
                        />{' '}
                        Альфа-Помощь
                    </Navbar.Brand>

                    <Form>
                        <Row>
                            <Col xs="auto">
                                <Button variant="outline-danger" href='/settings'>
                                    <i className="bi bi-gear"></i>
                                </Button>
                            </Col>
                            <Col xs="auto">
                                <ToggleButton id='toggle-check'
                                type="checkbox"
                                variant="outline-danger"
                                    onChange={handleChange}
                                    className="d-inline-block align-top"
                                    checked={localStorage.getItem("theme") == "dark"}
                                >
                                    <i className="bi bi-moon"></i>
                                </ToggleButton>
                            </Col>
                        </Row>
                    </Form>
                </Container>
            </Navbar>
            <h1>{greeting + last_part}</h1>
        </>
    );
}

export default Header