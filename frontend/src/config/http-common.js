export const host = 'http://localhost:8000/';
export const baseApiUrl = host + 'api/v1/';
export const loginUrl = baseApiUrl + 'auth/login/';
export const signupUrl = baseApiUrl + 'signup/';
export const profileUrl = baseApiUrl + 'users/me/';


export const getHeader = function () {
  const access_token = window.localStorage.getItem('token');
  const headers = {
    'Accept': 'application/json',
    'Authorization': 'Token ' + access_token
  };
  return headers
};
