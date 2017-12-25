<template>
  <div id="login">
    <div class="container">
      <h1 class="py-3">Login</h1>
      <form action="" class="">
        <div class="form-group row" v-for="(val,key) in signupForm">
          <label for="" class="col-3 col-form-label">{{unCamelCase(key)}}</label>
          <div class="col-9">
            <input class="form-control" type="text" v-model="signupForm[key]">
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
        </div>
        <button @click='login' class="btn btn-outline-success">Signup</button>
      </form>
    </div>
  </div>

</template>


<script>
  import axios from 'axios'
  import swal from 'sweetalert'

  export default {
    name: 'login',
    data() {

      return {
        signupForm: {
          username: '',
          password: '',
        },
        errors: {
          username: '',
          password: '',
        }
      }

    },
    methods: {
      login(event) {
        axios.post(`http://localhost:8000/api/v1/auth/login/`, {
          'username': this.signupForm.username,
          'password': this.signupForm.password,
        })
          .then(response => {
            console.log(response)
          }).catch(error => {
          const errors = error.response.data;
          console.log(errors);
          for (var v in errors) {
            if (v) {
              this.errors[v] = errors[v][0]
            }
          }
        });
        event.preventDefault()
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



