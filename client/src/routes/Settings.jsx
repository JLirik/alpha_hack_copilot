import { Container, Form, Button } from 'react-bootstrap';

function Settings() {
    return (<>
        <h1>Настройки</h1>
        <Form>
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
                    Сохранить
                </Button>
            </Form.Group>
            <Form.Group>
                <Button variant="secondary" href='/settings'>
                    Отменить изменения
                </Button>
            </Form.Group>
        </Form>
    </>)
}

export default Settings