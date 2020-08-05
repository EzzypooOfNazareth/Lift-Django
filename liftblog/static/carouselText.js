
  var carousel_text = new Vue({
    delimiters: ['<%', '%>'],
    el: '#carouselText',
    data: {
      messageText: ['Welcome', 'We\'re glad you\'re here!', 'Come learn the word of God', 'Transforming Lives'],
      timer: null,
      currentIndex: 0
    },
    mounted: function() {
      this.startSlide();
    },
    methods: {
      startSlide: function() {
        this.timer = setInterval(this.next, 4500);
      },
      next: function() {
        this.currentIndex += 1;
      },
    },
    computed: {
      currentText: function() {
        return this.messageText[Math.abs(this.currentIndex) % this.messageText.length]
      }
    }
  })
