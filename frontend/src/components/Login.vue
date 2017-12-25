<template>
  <div id="login">
    <div class="container">
      <h1 class="py-3">Login</h1>
      <form action="" class="">
        <div class="form-group row" v-for="(val,key) in signupForm">
          <label for="" class="col-3 col-form-label">{{unCamelCase(key)}}</label>
          <div class="col-9">
            <input class="form-control" type="text" v-model="signupForm[key]" @keyup="clearErrors(key)">
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-3">
          </div>
          <div class="col-9">
            <p class="small text-danger" v-if="errors.non_field_errors">{{ errors.non_field_errors}}</p>
          </div>
        </div>
        <button @click='login' class="btn btn-outline-success">Login</button>
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
          non_field_errors: ''


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
            this.$router.push('/dashboard')
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



