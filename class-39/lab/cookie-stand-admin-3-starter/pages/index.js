import { useState } from 'react'
import LoginForm from '../components/login-form'
import CookieStandAdmin from '../components/cookie-stand-admin'
import { fetcher } from '../services/data-fetcher'

export default function Home() {

    const [loggedIn, setLoggedIn] = useState(false);

    const [username, setUsername] = useState('');

    const [cookieStandHook, setCookieStandHook] = useState();

    const [error, setError] = useState()

    async function loginHandler(values) {

        try {

            setUsername(values.username);

            const hooks = await fetcher(values);

            setCookieStandHook(hooks);

            setLoggedIn(true);

            setError(null);

        } catch (err) {

            console.error(err);
            setError(err);
        }
    }

    function logoutHandler() {
        setLoggedIn(false);
        setCookieStandHook(null);
        setError(null);
        setUsername('');
    }

    if (!loggedIn) return <LoginForm onSubmit={loginHandler} error={error} />

    return <CookieStandAdmin
        useCookieStands={cookieStandHook.useCookieStands}
        onLogout={logoutHandler}
        username={username}
    />
}


