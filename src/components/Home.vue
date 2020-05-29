<template>
  <div class="hello">
    <div class="b-container">
       <slider/>
       <br>
       <b-container fluid="md">
        <b-row>
          <b-col sm="4">
              <b-card
              title="Card Title"
              img-src="../static/h1.jpeg"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2">
              <b-card-text>
                Some quick example text to build on the card title and make up the bulk of the card's content.
              </b-card-text>

          <b-button href="#" variant="primary">Read more</b-button>
           </b-card>
          </b-col>

          <b-col sm="4">
            <b-card
              title="Card Title"
              img-src="../static/3_68.jpeg"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2">
              <b-card-text>
                Some quick example text to build on the card title and make up the bulk of the card's content.
              </b-card-text>

              <b-button href="#" variant="primary">Read more</b-button>
        </b-card>
          </b-col>

          <b-col sm="4">
            <b-card
              title="Card Title"
              img-src="../static/h2_67.jpeg"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2">
              <b-card-text>
                Some quick example text to build on the card title and make up the bulk of the card's content.
              </b-card-text>
              <b-button href="#" variant="primary">Read more</b-button>
            </b-card>
          </b-col>
        </b-row>
        <br>
        <div class="container">
          <b-row>
            <b-col cols="12">
          <b-jumbotron class="myjumbo">
            <template v-slot:header><h3 style="color:#E13026">From mother nature</h3></template>

            <template v-slot:lead>

            </template>
            <p style="color:white">
              It uses utility classes for typography and spacing to space content out within the larger
              container.
            </p>
          </b-jumbotron>
            </b-col>
          </b-row>
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>
import slider from '@/components/slider.vue'

export default {
  name: 'Home',
  components: {
    slider
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.myjumbo{
  background-image: url('../static/gr1.jpg');
  border-radius: 4px;
  box-shadow: 0 4px 10px 4px rgba(19, 35, 47, 0.3);
}
</style>
