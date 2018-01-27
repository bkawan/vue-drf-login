export const apiDomain = 'http://localhost:8000/'
export const baseUrl = apiDomain + 'api/v1/'
export const loginUrl = baseUrl + 'auth/login/'


export const getHeader = function () {
  const access_token = window.localStorage.getItem('authUser')
  const headers = {
    'Accept': 'application/json',
    'Authorization': 'Token ' + access_token
  }
  return headers
}
