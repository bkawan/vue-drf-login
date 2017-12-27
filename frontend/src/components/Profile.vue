<template>
  <div id="profile">
    <div class="container py-3">
      <h3 class="text-center">Profile</h3>
      <div class="row" v-for="(v,k) in userDetail">
        <div class="col-md-3 text-right">{{unCamelCase(k)}} : </div>
        <div class="col-md-9">{{v}}</div>

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
          firstName: 'dsf',
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
//      getUserDetail() {
//        axios.get(`http://localhost:8000/api/v1/users/me/`).then(response => {
//          console.log(response)
//
//        }).catch(error => {
//          console.log(error)
//        })
//      },
      unCamelCase(value) {
        return value.replace(/([A-Z])/g, ' $1')
        // uppercase the first character
          .replace(/^./, function (str) {
            return str.toUpperCase();
          })
      }

    },
    created() {

      let token = localStorage.getItem('token');
      var t = 'Token ' + token;
      console.log(t)
      axios.get(`http://localhost:8000/api/v1/users/me/`, {
        headers: {
          Authorization: t
        }
      }).then(response => {
        this.userDetail.firstName = response.data.first_name;
        this.userDetail.lastName = response.data.last_name;
        this.userDetail.username = response.data.username;
        this.userDetail.gender = response.data.gender;
        this.userDetail.email = response.data.email;
        this.userDetail.salutation = response.data.salutation;
        this.userDetail.dateJoined = response.data.date_joined;
        console.log(response)

      }).catch(error => {
        console.log(error)
      })
    }
  }

</script>
