import { useEffect, useState } from 'react';
import { Container, Form, Button, Spinner } from 'react-bootstrap';
import { useNavigate } from 'react-router';
import fetcher from './methods/Fetcher';
import { AuthorizationError, RegistrationError } from './components/Errors';


function Settings() {
    const [settings, setSettings] = useState();

    useEffect(() => {
        async function loadSettings() {
            try {
                const response = await fetcher('settings', {}, 'GET');
                if (response) {
                    console.log(response);
                    setSettings(response);
                }
            } catch (err) {
                console.error(err);
                alert('Неизвестная ошибка')
            }
        }

        loadSettings()
    }, [])

    const updateSettings = async (event) => {
        const formData = new FormData(event.target);
        const username = formData.get("login");
        const password = formData.get("password");
        const city = formData.get("city");
        const business = formData.get("business");
        const name = formData.get("name");

        try {
            event.preventDefault();

            console.log(JSON.stringify({ username, password, city, name, business }));

            const response = await fetcher('settings', 'GET');
            if (response) {
                const data = await response.json();
                console.log(data);
            }
        } catch (err) {
            console.error(err);
            if (err === AuthorizationError) {
                alert("Неверный пароль");
            } else if (err === RegistrationError) {
                alert("Пользователь не найден");
            } else {
                alert('Неизвестная ошибка')
            }
        }
    };

    return (settings ?
        <>
            <h1>Настройки</h1>
            <Form onSubmit={updateSettings}>
                <Form.Group className="mb-3">
                    <Form.Control type="login" defaultValue={settings.username} name='login' required placeholder="Имя пользователя" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control type='password' name='password' required placeholder="Новый пароль (если хотите поменять)" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control defaultValue={settings.name} name='name' required placeholder="Фамилия Имя Отчество" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control defaultValue={settings.city} name='city' placeholder="Город работы" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control as={'textarea'} rows={5} defaultValue={settings.business} name='business' placeholder="Краткий рассказ о вашем бизнесе" />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Control type='password' name='curr_password' required placeholder="Старый пароль для подтверждения" />
                </Form.Group>
                <Form.Group>
                    <Button variant="primary" type='submit'>
                        Сохранить
                    </Button>
                </Form.Group>
                <Form.Group>
                    <Button variant="secondary" href='/'>
                        Отменить изменения
                    </Button>
                </Form.Group>
                <Form.Group>
                    <Button variant="danger" href='/auth'>
                        Выйти из аккаунта
                    </Button>
                </Form.Group>
            </Form>
        </> : <Spinner animation="border" />)
}

export default Settings;