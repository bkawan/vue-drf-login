<template>
  <div id="login">
    <div class="container p-lg-5 m-lg-5">
      <h1 class="py-3 text-center">Login</h1>
      <form action="" class="form-horizontal">
        <div class="form-group row" v-for="(val,key) in loginForm">
          <label for="" class="col-3 col-form-label text-right">{{unCamelCase(key)}} : </label>
          <div class="col-6">
            <input class="form-control" :type="loginForm[key].type" v-model="loginForm[key].value"
                   @keyup="clearErrors(key)">
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-3">
          </div>
          <div class="col-6">
            <p class="small text-danger" v-if="errors.non_field_errors">{{ errors.non_field_errors}}</p>
            <button @click='login' class="btn btn-outline-success float-right">Login</button>
          </div>

        </div>

        <div class="row pt-3">
          <div class="col-3"></div>
          <div class="col-6">
            <p class="small text-right">Don't have account ? <router-link to="signup">Register</router-link></p>
          </div>
        </div>
      </form>
    </div>
  </div>

</template>


<script>
  import axios from 'axios'
  import {loginUrl} from '../../config/http-common'
  import swal from 'sweetalert'

  export default {
    name: 'Login',
    data() {
      return {
        loginForm: {
          username: {
            value: '',
            type: 'text'
          },
          password: {
            value: '',
            type: 'password'
          },
        },
        errors: {
          username: '',
          password: '',
          non_field_errors: ''


        }
      }

    },
    methods: {
      login(event) {
        let authUser = ''
        axios.post(loginUrl, {
          'username': this.loginForm.username.value,
          'password': this.loginForm.password.value,
        })
          .then(response => {
            if(response.status === 200){
              alert(response)
              authUser = response.data.token
              window.localStorage.setItem('token',authUser)
            }
            this.$router.push('/dashboard/profile')
            // console.log(response);
            // localStorage.setItem('token', response.data.token);
            // this.$router.push('/dashboard/profile')
          }).catch(error => {
          const errors = error.response.data;
          console.log(errors);
          for (var v in errors) {
            if (v) {
              if (v == 'non_field_errors') {
                this.non_field_errors = errors[v][0]
              }
              this.errors[v] = errors[v][0]
            }
          }
        });
        event.preventDefault()
      },
      clearErrors(field) {
        this.errors[field] = '';
        this.errors.non_field_errors = '';

      },
      unCamelCase(value) {
        return value.replace(/([A-Z])/g, ' $1')
        // uppercase the first character
          .replace(/^./, function (str) {
            return str.toUpperCase();
          })
      }
    }

  }
</script>



