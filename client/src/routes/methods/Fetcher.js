import store from './store';
import { setAccessToken } from "./authSlice";
import { RegistrationError, AuthorizationError } from '../components/Errors';

const API_ADDRESS = 'http://89.223.124.107:8081/api/v1/';

export default async function fetcher(apiMethod, params = {}, method = 'POST') {
  let accessToken = store.getState().auth.accessToken;

  const callApi = async (token) => {
    let apiDict = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': token ? `Bearer ${token}` : undefined,
      }
    }
    if (method != 'GET') apiDict.body = JSON.stringify(params);
    const response = await fetch(API_ADDRESS + apiMethod, apiDict);

    if (response.status === 200) return await response.json();
    return null;
  };

  let result = accessToken ? await callApi(accessToken) : null;

  if (!result) {
    const refreshResponse = await fetch(API_ADDRESS + 'refresh', {
      method: 'GET',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
    });

    let newToken;

    if (refreshResponse.status === 200) {
      const data = await refreshResponse.json();
      newToken = data.accessToken;
    } else if (refreshResponse.status === 401) {
      throw AuthorizationError;
    } else {
      throw RegistrationError;
    }

    store.dispatch(setAccessToken(newToken));
    accessToken = newToken;

    result = await callApi(accessToken);
    if (!result) throw AuthorizationError;
  }

  return result;
}