require.config({
  paths: {
    jQuery: '/js/libs/jquery',
    Underscore: '/js/libs/underscore',
    Backbone: '/js/libs/backbone',
    text: '/js/libs/text',
    templates: '../templates'
  },

  shim: {
    'Backbone': ['Underscore', 'jQuery'],
    'PipeScan': ['Backbone']
  }
});

require(['PipeScan'], function(PipeScan) {
  PipeScan.initialize();
});
