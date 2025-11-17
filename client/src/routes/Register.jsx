import { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import Header from "../Header";
import { useNavigate } from 'react-router';
import { useDispatch } from 'react-redux';
import { setAccessToken } from './methods/authSlice';


function Register() {
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const [theme, setTheme] = useState(localStorage.getItem('theme'));
    document.querySelector("body").setAttribute("data-bs-theme", theme);

    const sentReg = async (event) => {
        const formData = new FormData(event.target);
        const username = formData.get("login");
        const password = formData.get("password");
        const city = formData.get("city");
        const business = formData.get("business");
        const name = formData.get("name");
        try {
            event.preventDefault();

            const response = await fetch('http://89.223.124.107:8081/api/v1/reg', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password, city, name, business })
            });
            if (response.status === 200) {
                const data = await response.json();
                const token = data.accessToken;
                dispatch(setAccessToken(token));
                navigate('/');
            } else if (response.status === 401) {
                alert("Неверный пароль");
            } else {
                alert("Пользователь не найден");
            }
        } catch (err) {
            console.error(err);
            alert("Ошибка сети");
        }
    };

    return (
        <Container fluid data-bs-theme={theme}>
            <Header themeHandle={setTheme} />
            <h1>Регистрация</h1>
            <Form onSubmit={sentReg}>
                <Form.Group className="mb-3">
                    <Form.Control type="login" name='login' required placeholder="Имя пользователя" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control type='password' name='password' required placeholder="Пароль" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control name='name' required placeholder="Фамилия Имя Отчество" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control name='city' placeholder="Город работы" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control as={'textarea'} rows={5} name='business' placeholder="Краткий рассказ о вашем бизнесе" />
                </Form.Group>
                <Form.Group>
                    <Button variant="primary" type='submit'>
                        Зарегистрироваться
                    </Button>
                </Form.Group>
                <Form.Group>
                    <Button variant="secondary" href='/auth'>
                        Войти в существующий аккаунт
                    </Button>
                </Form.Group>
            </Form>
        </Container>)
}

export default Register