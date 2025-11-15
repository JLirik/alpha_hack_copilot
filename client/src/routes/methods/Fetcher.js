export default async function fetcher(apiAddress, accessToken, params, method = 'POST') {
    const requestOptions = {
      method: method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify(params)
    };
    result = await fetch('http://127.0.0.1:4010/api/v1/' + apiAddress, requestOptions)
      .then(response => {
        if (response.status == 200) return response.json();
        else return null;
      })
    if (!result) {
        token = await fetch('http://127.0.0.1:4010/api/v1/refresh', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({user: localStorage.getItem("username")})
        })
      .then(response => {
        if (response.status == 200) return response.json().accessToken;
        else return null;
      })
      if (!token) throw Error.Authorization;
    }
    return result;
}