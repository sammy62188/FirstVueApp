<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="512"
      img-height="240"
      style="text-shadow: 1px 1px 2px #333;"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="First slide"
        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        img-src="../static/banner.jpg"
      ></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide img-src="../static/h2.jpg">
        <h1>Hello world!</h1>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide img-src='../static/h3.jpg'></b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
    </b-carousel>
  </div>
</template>
