<template>
  <div id="signup">
    <div class="container">
      <h1 class="py-3 text-center">Registration Form</h1>
      <form action="" class="" enctype="multipart/form-data">
        <div class="form-group row" v-for="(val, key) in signupForm">
          <label for="" class="col-3 col-form-label text-right">{{unCamelCase(key)}} : </label>
          <div class="col-6">
            <input class="form-control"
                   :type="signupForm[key].type"
                   v-model="signupForm[key].value"
                   @keyup="clearErrors(key)"
            >
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-3"></div>
          <div class="col-6">
            <p class="small text-danger" v-if="errors.nonFieldErrors">{{errors.nonFieldErrors}}</p>
            <button @click='signup' class="btn btn-outline-success float-right">Signup</button>
          </div>
        </div>
        <div class="row pt-3">
          <div class="col-3"></div>
          <div class="col-6">
            <p class="small text-right">Already have account ? <a href="../login">Login</a></p>
          </div>
        </div>
      </form>
    </div>
  </div>

</template>

<script>

  import axios from 'axios'
  import {signupUrl, getHeader} from '../../config/http-common'
  import swal from 'sweetalert'

  export default {
    name: 'Signup',
    data () {
      return {
        signupForm: {
          username: {
            value: '',
            type: 'text'
          },
          email: {
            value: '',
            type: 'email'
          },
          password: {

            value: '',
            type: 'password'
          },
          passwordAgain: {
            value: '',
            type: 'password'
          },
        },
        errors: {
          username: '',
          email: '',
          password: '',
          passwordAgain: '',
          nonFieldErrors: '',
        }
      }

    },
    methods: {
      signup (event) {
        axios.post(signupUrl, {
          'username': this.signupForm.username.value,
          'email': this.signupForm.email.value,
          'password': this.signupForm.password.value,
          'password_again': this.signupForm.passwordAgain.value,
        })
          .then(response => {
            console.log(response);
            this.$router.push({name: 'login'})
          }).catch(error => {
          const errors = error.response.data;
          console.log(errors)
          for (var v in errors) {

            if (v) {
              if (v == 'password_again') {
                this.errors.passwordAgain = errors[v][0]
              }
              if (v == 'non_field_errors') {

                this.errors.passwordAgain = errors[v][0]
              }
              this.errors[v] = errors[v][0]
            }
          }


        });

        event.preventDefault()


      },
      unCamelCase (value) {
        return value.replace(/([A-Z])/g, ' $1')
        // uppercase the first character
          .replace(/^./, function (str) {
            return str.toUpperCase();
          })
      },
      clearErrors (field) {
        this.errors[field] = '';
        this.errors.nonFieldErrors = '';

      },
    }

  }
</script>



