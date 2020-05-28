<template>
  <div class="myform">
    <b-container class="mycon">
    <div class="myclass">
       <div class="vl">
        <span class="vl-innertext">or</span>
      </div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-row>
        <b-col>
            <b-form-group id="input-group-2">
              <b-form-input
                id="input-2"
                v-model="form.name"
                required
                placeholder="Name">
                </b-form-input>
            </b-form-group>

             <b-form-group
              id="input-group-1">
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                required
                placeholder="Email"
              ></b-form-input>
            </b-form-group>

             <b-form-group
              id="input-group-6">
              <b-form-input
                id="input-6"
                v-model="form.tel"
                type="tel"
                required
                placeholder="Phone Number"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-3">
        <b-form-input
          id="input-3"
          v-model="form.Information"
          :options="Information"
          placeholder="Subject"
          required>
        </b-form-input>
      </b-form-group>
          <b-form-group id="input-group-5">
              <b-textarea v-model="form.message" id="message"
              type="textarea"
              placeholder="Message">
              </b-textarea>
          </b-form-group>

           <b-button-group>
          <b-button type="submit" variant="primary" id="mysub">Submit</b-button>
          <b-button type="reset" variant="danger" id="myre">Cancel</b-button>
          </b-button-group>
        </b-col>

        <b-col>
            <h2 style="margin-top:-35px">CONTACT</h2>
            <p> Any Questions?<br><br>
                Feel free to call us, if not send us<br>
                a message and we will be happy to reply you<br>
                as soon as possible.<br><br>
                Tel: +2348026359631 <br> +234802230670<br><br>
                Email: labsanfoodslimited@gmail.com
            </p>
        </b-col>
      </b-row>
    </b-form>
    </div>
  </b-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      form: {
        email: '',
        name: '',
        tel: '',
        Information: null,
        message: ''
      },
      Information: [{ text: 'Select One', value: null }, 'Friends', 'Website', 'Other'],
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      axios.post('http://localhost:5000/api/regis', {
        name: this.form.name,
        email: this.form.email,
        tel: this.form.tel,
        message: this.form.message,
        Information: this.form.Information
      }).then(response => {
        alert('Thanks for your feedback')
        this.$router.push('/')
      }).catch(error => {
        console.log(error)
      })
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.name = ''
      this.form.tel = ''
      this.form.Information = null
      this.form.message = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style scoped>
.myform{
    border: 2px;
}
#mysub{
  margin: 5px;
}

#myre{
  margin: 5px;
}
h2{
  margin: 10px;
  padding: 5px;
  color: deeppink;
  font-family: Georgia, 'Times New Roman', Times, serif;
}
.myclass{
  width: 80%;
  margin: 50px;
  padding: 50px;
  border-radius: 6px;
  box-shadow: 0 4px 10px 4px rgba(19, 35, 47, 0.3);
  background-color: #f2f2f2;
}
.mycon{
  position: relative;
   border-radius: 5px;
}
.vl {
  position: absolute;
  left: 46%;
  transform: translate(-50%);
  border: 2px solid #ddd;
  height: 375px;
}

/* text inside the vertical line */
.vl-innertext {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  background-color: #f1f1f1;
  border: 1px solid #ccc;
  border-radius: 50%;
  padding: 8px 10px;
}
</style>
