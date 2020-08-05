window.onload = function() {
  var burger = new Vue({
    el: '#burger-menu',
    data: {
      show: false
    },
    methods: {
      toggleShow: function () {
        this.show = !this.show;
      }
    }
  })
}
