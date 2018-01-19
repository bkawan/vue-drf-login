export const STORAGE_KEY = 'drf-vue-project'

let syncedData = {
  auth: {
    isLoggedIn: false,
    accessToken: null
  },
  user: {
    name: null
  }
}

// Sync with local storage.
if (localStorage.getItem(STORAGE_KEY)) {
  syncedData = JSON.parse(localStorage.getItem(STORAGE_KEY))
}

// Merge data and export it.
export const state = Object.assign(syncedData)
