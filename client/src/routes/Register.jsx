import { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import Header from "../Header";

function Register() {
  const [theme, setTheme] = useState(localStorage.getItem('theme'));

    const sentReg = (formData) => {
        token = fetch('http://127.0.0.1:4010/api/v1/reg', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user: localStorage.getItem("username") })
        })
            .then(response => {
                if (response.status == 200) return response.json().accessToken;
                else return null;
            })
        if (!token) throw Error.Authorization;
        
        return token;
    }

  return (
        <Container fluid data-bs-theme={theme}>
            <Header themeHandle={setTheme} />
            <h1>Регистрация</h1>
            <Form action={sentReg}>
                <Form.Group className="mb-3">
                    <Form.Control type="login" required placeholder="Имя пользователя" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control type='password' required placeholder="Пароль" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control placeholder="Город работы" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control as={'textarea'} rows={5} placeholder="Краткий рассказ о вашем бизнесе" />
                </Form.Group>
                <Form.Group>
                    <Button variant="primary" type='submit'>
                        Зарегистрироваться
                    </Button>
                </Form.Group>
                <Form.Group>
                    <Button variant="secondary" href='/reg'>
                        Войти
                    </Button>
                </Form.Group>
            </Form>
        </Container>)
}

export default Register