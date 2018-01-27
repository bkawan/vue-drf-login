<template>
  <div id="profile">
    <div class="container py-3">
      <div class="row">
        <div class="col-md-3">
        </div>
        <div class="col-md-9">
          <div class="card text-gray-dark">
            <div class="media p-2">
              <img class="d-flex mr-3"
                   :src="userDetail.avatar"
                   :alt="userDetail.firstName + ' ' + userDetail.lastName"
                   height="84"
                   width="84"
              >
              <div class="media-body">
                <h5 class="mt-0">{{userDetail.salutation}} {{userDetail.firstName}} {{ userDetail.lastName}}
                  <span class="float-right"><router-link to="/dashboard/profile/edit/" class="pr-3 btn btn-primary">Edit</router-link></span></h5>
                Username : <strong>{{userDetail.username}}</strong>
                <br>
                <i class="fa fa-envelope"></i> Email: <strong> {{userDetail.email}}</strong>
                <br>
                <i class="fa fa-male"></i> Gender: <strong> {{userDetail.gender}}</strong>
                <br>
                <i class="fa fa-mobile-phone"></i> Mobile: <strong> {{userDetail.mobile}}</strong>
                <br>
                <i class="fa fa-clock-o"></i> Date Joined: <strong> {{userDetail.dateJoined | fromNow}}</strong>
                <br>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

  import axios from 'axios'
  import {baseUrl, getHeader} from '../../config/http-common'
  import moment from 'moment'

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
      unCamelCase(value) {
        return value.replace(/([A-Z])/g, ' $1')
        // uppercase the first character
          .replace(/^./, function (str) {
            return str.toUpperCase();
          })
      }
    },
    filters: {
      fromNow(value) {
        return moment(value).fromNow()
      }
    },
    created() {
      axios.get(baseUrl+`users/me/`,{headers: getHeader()}).then(response => {
        this.userDetail.firstName = response.data.first_name;
        this.userDetail.lastName = response.data.last_name;
        this.userDetail.username = response.data.username;
        this.userDetail.gender = response.data.gender;
        this.userDetail.email = response.data.email;
        this.userDetail.salutation = response.data.salutation;
        this.userDetail.dateJoined = response.data.date_joined;
        this.userDetail.avatar = response.data.avatar;
        this.userDetail.mobile = response.data.mobile;
        console.log(response)

      }).catch(error => {
        console.log(error)
      })
    }
  }

</script>
