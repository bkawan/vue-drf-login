<template>
  <div id="signup">
    <div class="container">
      <h1 class="py-3 text-center">Edit Profile</h1>
      <form action="" class="" enctype="multipart/form-data">
        <div class="form-group row" v-for="(val, key) in profileEditForm">
          <label for="" class="col-3 col-form-label text-right">{{unCamelCase(key)}} : </label>
          <div class="col-6" v-if="profileEditForm[key].type === 'radio'">
            <input class=""
                   type="radio"
                   id="male"
                   value="Male"
                   v-model="profileEditForm[key].value"
                   @click="clearErrors(key)"
            >
            <label for="male">Male</label>
            <br>
            <input type="radio"
                   id="female"
                   value="Female"
                   v-model="profileEditForm[key].value"
                   @click="clearErrors(key)"
            >
            <label for="female">Female</label>
            <br>
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
          <div class="col-6" v-else-if="profileEditForm[key].type=='select'">
            <select name="" id=""
                    v-model="profileEditForm[key].value"
                    @click="clearErrors(key)"
            >
              <option v-for="option in profileEditForm[key].options"
                      :value="option"

              >
                {{option}}
              </option>
            </select>
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
          <div class="col-6" v-else>
            <input class="form-control"
                   :type="profileEditForm[key].type"
                   v-model="profileEditForm[key].value"
                   @keyup="clearErrors(key)"
            >
            <p class="small text-danger" v-if="errors[key]">{{errors[key]}}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-3"></div>
          <div class="col-6">
            <input type="file" accept="image/*" @change="onFileChange" :value="avatar">
            <img :src="avatar" alt="">
            <button @click='signup' class="btn btn-outline-success float-right">Save</button>
          </div>
        </div>
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
        profileEditForm: {
          salutation: {
            value: '',
            type: 'select',
            options: [
              "Mr",
              "Miss",
            ]
          },
          firstName: {
            value: '',
            type: 'text'
          },
          lastName: {

            value: '',
            type: 'text'
          },
          gender: {
            value: '',
            type: 'radio',
            options: ['Male', 'Female', 'Others']
          },
          username: {
            value: '',
            type: 'text'
          },
          email: {
            value: '',
            type: 'email'
          },
          avatar: 'sdf'
        },
        errors: {
          firstName: '',
          lastName: '',
          username: '',
          email: '',
          gender: '',
          salutation: '',
        }
      }

    },
    methods: {
      signup(event) {
        axios.put(`http://localhost:8000/api/v1/users/`, {
          'first_name': this.profileEditForm.firstName.value,
          'last_name': this.profileEditForm.lastName.value,
          'salutation': this.profileEditForm.salutation.value,
          'gender': this.profileEditForm.gender.value,
          'username': this.profileEditForm.username.value,
          'email': this.profileEditForm.email.value,
          'avatar': this.avatar,
        })
          .then(response => {
            console.log(response);
            this.$router.push('/login')
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
      },
      clearErrors(field) {
        this.errors[field] = '';
        this.errors.non_field_errors = '';

      },
      onFileChange(event) {
        let files = event.target.files;
        if (!files.length)
          return;

        this.createImage(files[0])
      },
      createImage(file) {
        let image = new Image();
        let reader = new FileReader();

        reader.onload = (e) => {
          let vm = this;
          vm.avatar = e.target.result;
          console.log(e.target.result)
        },
          reader.readAsDataURL(file);


      }

    }

  }
</script>


