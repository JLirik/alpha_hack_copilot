import { Container, Form, Button, Alert } from 'react-bootstrap';
import Header from "../Header";
import { useNavigate } from 'react-router';
import { useDispatch } from 'react-redux';
import { setAccessToken } from './methods/authSlice';
import { useState } from 'react';

function Login() {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const [errorMessage, setErrorMessage] = useState(null);

    const [theme, setTheme] = useState(localStorage.getItem('theme'));
    document.querySelector("body").setAttribute("data-bs-theme", theme);

    const sentAuth = async (event) => {
        event.preventDefault();

        const formData = new FormData(event.target);
        const username = formData.get("login");
        const password = formData.get("password");

        try {
            const response = await fetch('http://127.0.0.1:4010/api/v1/auth', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password })
            });
            console.log(JSON.stringify({ username, password }));
            if (response.status === 200) {
                const data = await response.json();
                console.log(data)
                const token = data.accessToken;
                dispatch(setAccessToken(token));
                navigate('/');
            } else if (response.status === 401) {
                setErrorMessage("Неверный пароль");
            } else {
                setErrorMessage("Пользователь не найден");
            }
        } catch (err) {
            console.error(err);
            setErrorMessage("Ошибка сети");
        }
    };

    return (
        <Container fluid data-bs-theme={theme}>
            <Header themeHandle={setTheme} />
            <h1>Логин</h1>
            {errorMessage && (
                <Alert variant="danger" onClose={() => setErrorMessage(null)} dismissible>
                    {errorMessage}
                </Alert>
            )}
            <Form onSubmit={sentAuth}>
                <Form.Group className="mb-3">
                    <Form.Control name="login" type="text" required placeholder="Имя пользователя" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control name="password" type="password" required placeholder="Пароль" />
                </Form.Group>
                <Form.Group>
                    <Button variant="primary" type="submit">Войти</Button>
                </Form.Group>
                <Form.Group>
                    <Button variant="secondary" href='/reg'>Зарегистрироваться</Button>
                </Form.Group>
            </Form>
        </Container>
    );
}

export default Login;