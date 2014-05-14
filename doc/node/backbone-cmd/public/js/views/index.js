define(['text!templates/index.html'], function(indexTemplate) {

  getResults = function() {
      var execSync = require('exec-sync');   
      var text = execSync('echo $USER');
      var files = execSync('ls');
      return "<h1>"+text+"</h1><pre>"+files+"</pre>"
  };
    
  var indexView = Backbone.View.extend({
    el: $('#content'),

    render: function() {
        var templateArgs = {
          name: "Bogus name",
        };
        $(this.el).html(this.template(templateArgs));

        //this.$el.html('My Name');
        //this.$el.html(indexTemplate);
        // 'Posted from Backbone view: index.js'+${files}); //  getResults()
    }
  });

  return new indexView;
});
