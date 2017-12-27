<template>
  <div id="profile">
    <div class="container py-3">
      <h3>Dashboard</h3>
      <div class="row" v-for="(v,k) in userDetail">
        <div class="col-md-3">{{unCamelCase(k)}}</div>
        <div class="col-md-9">:{{v}}</div>

      </div>
    </div>
  </div>
</template>


<script>

  import axios from 'axios'

  export default {

    data() {

      return {
        userDetail: {
          salutation: '',
          gender: '',
          firstName: '',
          lastName: '',
          email: '',
          username: '',
          avatar: '',
          mobile: '',
          dateJoined: '',
        }
      }
    },
    methods: {
      getUserDetail() {
        axios.get(`http://localhost:8000/api/v1/users/me/profile/`).then(response => {
          console.log(response)

        }).catch(error => {
          console.log(error)
        })
      },
      unCamelCase(value) {
        return value.replace(/([A-Z])/g, ' $1')
        // uppercase the first character
          .replace(/^./, function (str) {
            return str.toUpperCase();
          })
      }

    },
    created() {
      axios.get(`http://localhost:8000/api/v1/users/me`).then(response => {
        console.log(response)

      }).catch(error => {
        console.log(error)
      })
    }
  }

</script>
