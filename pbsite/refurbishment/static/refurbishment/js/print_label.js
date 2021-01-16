$( ".ref_label" ).click(function() {
    this.label_number = 3;
  this.label_url = $(this).data("label_url") + '?n=' + this.label_number;
  window.open(this.label_url).print();
});