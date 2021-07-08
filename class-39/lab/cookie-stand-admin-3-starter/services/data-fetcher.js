import axios from 'axios'
import useSWR from 'swr'

// TODO: ask API team to supply hours array
const hours = ['6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm'];

const baseUrl = 'https://cookie-stand-api.herokuapp.com';
const tokenUrl = baseUrl + '/api/token/';
const refreshUrl = tokenUrl + 'refresh'; // GOTCHA: no trailing slash
export const apiUrl = baseUrl + '/api/v1/cookie-stands/';

// get a JSON Web Token from server
export async function getToken(values) {

    const response = await axios.post(tokenUrl, values);

    const refreshResponse = await axios.post(refreshUrl, { refresh: response.data.refresh });

    return refreshResponse.data.access;
}

// expose useCookieStands with token enclosed
export async function fetcher(values) {

    const token = await getToken(values);

    return {
        useCookieStands: () => useCookieStands(token),
    }
}

function useCookieStands(token) {
    const { data, error, mutate } = useSWR([apiUrl, token], fetchWithToken);

    return {
        cookieStands: data,
        error,
        createStand: (values) => createStand(values, data, mutate, token),
        deleteStand: (stand) => deleteStand(stand, data, mutate, token),
        updateStand: (stand) => updateStand(stand, data, mutate, token),
    }
}

async function createStand(values, data, mutate, token) {

    const newStand = CookieStand.fromValues(values);

    newStand.location += '...'; // Add the ... to show loading state

    const updatedStands = [newStand, ...data];

    mutate(updatedStands, false);

    await postWithToken(token, values);

    mutate();
}

async function updateStand(stand, data, mutate, token) {
    // TODO: stretch goal
}

async function deleteStand(stand, data, mutate, token) {

    const updatedStands = data.filter(storedStand => storedStand.id !== stand.id);

    mutate(updatedStands, false);

    await deleteWithToken(stand.id, token);

    mutate(async stands => {
        return stands.filter(candidate => candidate.id !== stand.id);
    });
}
// Common practice to have a "Data Access Object" to encapsulate fetched data
class CookieStand {

    constructor(info) {
        this.id = info.id;
        this.location = info.location;
        this.minCustomersPerHour = info.minimum_customers_per_hour;
        this.maxCustomersPerHour = info.maximum_customers_per_hour;
        this.avgCookiesPerSale = info.average_cookies_per_sale;
        this.cookiesEachHour = info.hourly_sales || [...hours].fill(0);
        this.totalDailyCookies = this.cookiesEachHour.reduce((sum, val) => sum + val);
    }

    static fromValues(values) {
        const info = {
            id: -1, // will be overwritten once cache revalidates
            location: values.location,
            minimum_customers_per_hour: values.min,
            maximum_customers_per_hour: values.max,
            average_cookies_per_sale: values.avg,
        }

        return new CookieStand(info);
    }
}



// GET from API with authentication
async function fetchWithToken(url, token) {

    const config = makeConfig(token);

    const response = await axios.get(url, config);

    const stands = response.data.map(info => new CookieStand(info));

    // Sort alphabetically
    stands.sort((a, b) => {
        if (a.location < b.location) return -1;
        if (a.location > b.location) return 1;
        return 0;
    });

    return stands;
}


// POST to API with authentication
async function postWithToken(token, values) {

    const body = {
        id: -1, // will be overwritten once cache revalidates
        location: values.location,
        minimum_customers_per_hour: values.min,
        maximum_customers_per_hour: values.max,
        average_cookies_per_sale: values.avg,
    }

    const config = makeConfig(token);

    const response = await axios.post(apiUrl, body, config);

    return response.data;
}

async function deleteWithToken(id, token) {
    const config = makeConfig(token);

    const url = apiUrl + id + '/';

    await axios.delete(url, config);

}

// helper function to handle getting Authorization headers EXACTLY right
function makeConfig(token) {
    return {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    }
}
