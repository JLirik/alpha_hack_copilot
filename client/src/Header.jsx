import './App.css'
import { Col, Container, Form, Nav, Navbar, NavDropdown, Row, Button } from 'react-bootstrap';

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
                    <Navbar.Brand href="/">Альфа-Помощь</Navbar.Brand>

                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link href="#home">Home</Nav.Link>
                            <Nav.Link href="#link">Link</Nav.Link>
                            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.2">
                                    Another action
                                </NavDropdown.Item>
                                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                                <NavDropdown.Divider />
                                <NavDropdown.Item href="#action/3.4">
                                    Separated link
                                </NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                        <Form>
                            <Row>
                                <Col xs="auto">
                                    <Button variant="outline-primary" href='/settings'>
                                        <i className="bi bi-gear"></i>
                                    </Button>
                                </Col>
                                <Col xs="auto">
                                    <Form.Switch
                                        id="theme-switch"
                                        onChange={handleChange}
                                        checked={localStorage.getItem("theme") == "dark"}
                                    />
                                </Col>
                            </Row>
                        </Form>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <h1>{greeting + last_part}</h1>
        </>
    );
}

export default Header