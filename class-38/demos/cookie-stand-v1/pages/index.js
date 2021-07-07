import Head from 'next/head'
import { useState } from 'react'

export default function Home() {

    const [stand, setStand] = useState({ "status": "pending" });

    function submitHandler(event) {
        event.preventDefault();
        const standInfo = {};
        standInfo.location = event.target.location.value;
        standInfo.minCustomers = parseInt(event.target.minCustomers.value);
        standInfo.maxCustomers = parseInt(event.target.maxCustomers.value);
        standInfo.avgCookies = parseFloat(event.target.avgCookies.value);

        setStand(standInfo);
    }

    return (
        <div>
            <Head>
                <title>Cookie Stand Admin</title>
            </Head>
            <header className="p-6 bg-green-500">
                <h1 className="text-2xl font-semibold">Cookie Stand Admin</h1>
            </header>
            <main>
                <form className="w-2/3 py-2 mx-auto my-8 bg-green-200" onSubmit={submitHandler}>
                    <fieldset className="w-full p-2">
                        <legend className="text-xl font-semibold text-center">Create Cookie Stand</legend>
                        <div className="flex">
                            <label className="" htmlFor="location">Location</label>
                            <input className="flex-auto" id="location" name="location" type="text" />
                        </div>
                        <div className="flex gap-4">

                            <div className="flex-1">
                                <label htmlFor="min-customers">Minimum Customers per Hour</label>
                                <input id="min-customers" name="minCustomers" type="number" required />
                            </div>
                            <div className="flex-1">
                                <label htmlFor="max-customers">Maximum Customers per Hour</label>
                                <input id="max-customers" name="maxCustomers" type="number" required />
                            </div>
                            <div className="flex-1">
                                <label htmlFor="avg-cookies">Average Cookies per Sale</label>
                                <input id="avg-cookies" name="avgCookies" type="number" step=".1" required />
                            </div>
                            <button className="flex-1 py-2 bg-green-500 rounded">Create</button>
                        </div>
                    </fieldset>
                </form>
                <pre className="text-center">
                    <code>
                        {JSON.stringify(stand)}
                    </code>
                </pre>
            </main>
            <footer className="py-6 pl-6 bg-green-500">
                <p>&copy; 2021</p>
            </footer>
        </div>
    )
}
