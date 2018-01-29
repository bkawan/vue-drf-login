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
            <p class="small text-danger" v-if="errors.avatar">{{errors.avatar}}</p>
            <button @click='signup' class="btn btn-outline-success float-right">Save</button>
          </div>
        </div>
      </form>
    </div>
  </div>

</template>

<script>
  import axios from 'axios'
  import {profileUrl, getHeader} from '../../config/http-common'
  import swal from 'sweetalert'

  export default {
    data () {
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
          mobile: {
            value: '',
            type: 'text'
          },
        },
        avatar: '',
        errors: {
          firstName: '',
          lastName: '',
          username: '',
          email: '',
          gender: '',
          salutation: '',
          mobile: '',
          avatar: ''
        }
      }

    },
    methods: {
      signup (event) {
        console.log(getHeader())
        axios.put(profileUrl, {
          'first_name': this.profileEditForm.firstName.value,
          'last_name': this.profileEditForm.lastName.value,
          'salutation': this.profileEditForm.salutation.value,
          'gender': this.profileEditForm.gender.value,
          'username': this.profileEditForm.username.value,
          'email': this.profileEditForm.email.value,
          'mobile': this.profileEditForm.mobile.value,
          'avatar': this.avatar,
        }, {headers: getHeader()})
          .then(response => {
            console.log(response)
            window.history.length > 1
              ? this.$router.go(-1)
              : this.$router.push({name: 'profile'});

          }).catch(error => {
          console.log(error)
          const _errors = error.response.data;

          for (var v in _errors) {
            if (v) {
              if (v == 'first_name') {
                this.errors.firstName = _errors[v][0]
              }
              if (v == 'last_name') {
                this.errors.lastName = _errors[v][0]
              }
              this.errors[v] = _errors[v][0]
            }
          }

        });

        event.preventDefault();
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
        this.errors.non_field_errors = '';

      },
      onFileChange (event) {
        let form = new FormData();
        let files = event.target.files || e.dataTransfer.files;
        console.log(files);
        if (!files.length)
          return;
        this.createImage(files[0])
      },
      createImage (file) {

        let image = new Image();
        let reader = new FileReader();
        reader.onload = (e) => {
          let vm = this;
          vm.avatar = e.target.result;
          reader.readAsDataURL(file);

        }
      }

    },
    created () {
      axios.get(profileUrl, {headers: getHeader()}).then(response => {
        this.profileEditForm.firstName.value = response.data.first_name;
        this.profileEditForm.lastName.value = response.data.last_name;
        this.profileEditForm.username.value = response.data.username;
        this.profileEditForm.gender.value = response.data.gender;
        this.profileEditForm.email.value = response.data.email;
        this.profileEditForm.salutation.value = response.data.salutation;
        this.profileEditForm.mobile.value = response.data.mobile;
        this.avatar = response.data.avatar;
//        this.avatar = this.createImage(this.$refs.cropper.replace(response.data.avatar));
      }).catch(error => {
        console.log(error)
      })
    }

  }
</script>


