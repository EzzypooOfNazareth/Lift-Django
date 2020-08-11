const donation = new Vue({
  delimiters: ['<%', '%>'],
  el: '#donation',
  data: {
    screenState: true,
    amount: 0
  },
  methods: {
    changeState: function() {
      this.amount = document.getElementById('amount').value;
      console.log(this.amount)
      this.screenState = false;
    }
  }
})
