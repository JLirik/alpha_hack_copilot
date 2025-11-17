import store from './store';
import { setAccessToken } from "./authSlice";

export default async function fetcher(apiMethod, params, method = 'POST') {
  let accessToken = store.getState().accessToken;
  const apiAddress = 'http://127.0.0.1:4010/api/v1/';
  const requestOptions = {
    method: method,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${accessToken}`,
    },
    body: JSON.stringify(params)
  };

  result = (accessToken && await fetch(apiAddress + apiMethod, requestOptions)
    .then(response => {
      if (response.status == 200) return response.json();
      else return null;
    }))
  if (!result) {
    token = await fetch(apiAddress + 'refresh', {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user: localStorage.getItem("username") })
    })
      .then(response => {
        if (response.status == 200) return response.json().accessToken;
        else if (response.status == 401) return null;
        else return 1;
      })
    if (!token) throw Error.Authorization;
    if (token == 1) throw Error.Registration
    store.dispatch(setAccessToken(token));
    accessToken = token;
  }
  result = await fetch(apiAddress + apiMethod, requestOptions)
    .then(response => {
      if (response.status == 200) return response.json();
      else throw Error.Authorization;
    })
  return result;
}