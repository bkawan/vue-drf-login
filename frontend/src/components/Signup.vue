<template>
  <div id="signup">
    <div class="container">

      <form action="" class="">
        <div class="form-group row" v-for="(val,key) in signupForm">
          <label for="" class="col-3 col-form-label">{{unCamelCase(key)}}</label>
          <div class="col-9">
            <input class="form-control" type="text" v-model="signupForm[key]">
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
        }
      }

    },
    methods: {
      signup(event) {
        console.log('here')
        axios.post(`http://localhost:8000/api/v1/users/`,this.signupForm)
          .then(response => {
            console.log(response)
          })

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



