<template>
  <div class="header">
   <b-navbar type="dark" toggleable="md" variant="dark">
     <b-navbar-brand to="/"><img src="../static/logo.png" alt="" id="myimg"></b-navbar-brand>
      <b-navbar-nav>
     <!-- <b-nav-item to="/">Home</b-nav-item>-->

      <b-nav-item to="/about"> About</b-nav-item>
            <b-nav-item-dropdown text="Product" left>
        <b-dropdown-item to="/garri">Garri</b-dropdown-item>
        <b-dropdown-item to="/honey">Honey</b-dropdown-item>
        <b-dropdown-item to="/groundnut">Groundnut</b-dropdown-item>
      </b-nav-item-dropdown>
      <b-nav-item to="/contact">Contact</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
  </div>
</template>

<style scoped>
h2{
  color: #009999 ;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.header{
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
  z-index: 1;
}
#myimg{
  margin: 5px;
}
</style>
