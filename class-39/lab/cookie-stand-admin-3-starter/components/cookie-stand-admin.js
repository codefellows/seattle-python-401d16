import Head from 'next/head'
import CookieStandForm from './cookie-stand-form'
import CookieStandTable from './cookie-stand-table'
import CookieStandHeader from './cookie-stand-header'
import CookieStandFooter from './cookie-stand-footer'

export default function CookieStandAdmin({ onLogout, username, useCookieStands }) {

    const { cookieStands, error, createStand, deleteStand } = useCookieStands();

    if (error) {
        onLogout();
        return null;
    }

    if (!cookieStands) return <h2>Loading...</h2>

    return (
        <div>
            <Head>
                <title>Cookie Stand Admin</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <CookieStandHeader username={username} onLogout={onLogout} />

            <main className="w-5/6 mx-auto">
                <CookieStandForm onCreate={createStand} />
                <CookieStandTable stands={cookieStands} onDelete={deleteStand} />
            </main>

            <CookieStandFooter reports={cookieStands} />
        </div>
    )
}
