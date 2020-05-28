<template>
  <div class="footer">
    <b-container>
      <b-row>
        <b-col>
          <h3><img src="../static/email.png" alt=""></h3>
          <a href ="labsanfoodslimited@gmail.com">labsanfoodslimited@gmail.com</a>
        </b-col>
        <b-col>
          <h3><img src="../static/location.png" alt="" class="img1"></h3>
          <p> 3, Babatunde Sanni Close,<br>
          Peace Estate,<br>
          Off Eammnuel Bus Stop,<br>
          Ajuwon Akute Road,<br>
          Ogun State</p><br>
        </b-col>
        <b-col>
          <h3><img src="../static/call.png" alt="" class="img2"></h3>
          <p>08026359631, 0802230670</p>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style scoped>
.footer{
  bottom: 0;
  width: 100%;
  height: 250px;
  background-color: #1E1E1E;
  position: relative;
}
h3{
  font-family: Georgia, 'Times New Roman', Times, serif;
  color: deeppink;
  padding-top: 45px;
}

p{
  padding-top: 1px;
  color: white;
  font-size: 0.9em;
  font-family: Georgia, 'Times New Roman', Times, serif;
}
a{
  color: white;
  font-size: 0.9em;
  font-family: Georgia, 'Times New Roman', Times, serif;
}
.img1{
  background-color: white;
}
.img2{
  color: white;
}
</style>
