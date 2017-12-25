<template>
  <div id="signup">
    <div class="container">

      <form action="" class="">
        <div class="form-group row" v-for="(val,key) in signupForm">
          <label for="" class="col-3 col-form-label">{{unCamelCase(key)}}</label>
          <div class="col-9">
            <input class="form-control" type="text" v-model="signupForm[key]">
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
        </div>
        <button @click='signup' class="btn btn-outline-success">Signup</button>
      </form>
    </div>
  </div>

</template>


<script>
  import axios from 'axios'
  import swal from 'sweetalert'

  export default {
    name: 'signup',
    data() {

      return {
        signupForm: {
          firstName: '',
          lastName: '',
          username: '',
          email: '',
          password: '',
          passwordAgain: '',
        },
        errors: {
          firstName: '',
          lastName: '',
          username: '',
          email: '',
          password: '',
          passwordAgain: '',
        }
      }

    },
    methods: {
      signup(event) {
        axios.post(`http://localhost:8001/api/v1/users/`, {
          'first_name': this.signupForm.firstName,
          'last_name': this.signupForm.lastName,
          'username': this.signupForm.username,
          'email': this.signupForm.email,
          'password': this.signupForm.password,
          'password_again': this.signupForm.passwordAgain,
        })
          .then(response => {
            console.log(response)
          }).catch(error => {
          const errors = error.response.data
          for (var v in errors) {
            if (v) {
              if (v == 'first_name') {
                this.errors.firstName = errors[v][0]
              }
              if (v == 'last_name') {
                this.errors.lastName = errors[v][0]
              }
              if (v == 'username') {
                this.errors.username = errors[v][0]
              }
              if (v == 'email') {
                this.errors.email = errors[v][0]
              }
              if (v == 'password') {
                this.errors.password = errors[v][0]
              }
              if (v == 'password_again') {
                this.errors.passwordAgain = errors[v][0]
              }

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



