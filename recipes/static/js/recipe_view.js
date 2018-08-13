(function (jQuery) {
  jQuery.mark = {
    makecookinglist: function (options) {
      var defaults = {
        selector: '.cooking-list'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var cooklistobj = jQuery(this);
        var getTheId = "method-list";
        if (localStorage.getItem(String('cooking-list'))) {
          cooklistobj.html(localStorage.getItem('cooking-list'));
        } else if (localStorage.getItem(String(getTheId)))  {           
          cooklistobj.html(localStorage.getItem(getTheId));
        } else {
          cooklistobj.html(jQuery('#method-list').html());
        }
      })
    },
    makeshoppinglist: function (options) {
      var defaults = {
        selector: '.shopping-list'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var shoplistobj = jQuery(this);
        var getTheId = "ingredients-list";
        if (localStorage.getItem(String('shopping-list'))) {
          shoplistobj.html(localStorage.getItem('shopping-list'));
        } else if (localStorage.getItem(String(getTheId)))  {           
          shoplistobj.html(localStorage.getItem(getTheId));
        } else {
          shoplistobj.html(jQuery('#ingredients-list').html());
        }
      })
    },
    cookcheck: function (options) {
      var defaults = {
        selector: '.cooking-list'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var cookobj = jQuery(this);
        cookobj.on( "click", "li", function() {
          jQuery(this).toggleClass("fade-me");
          var getcooking = jQuery(this).parent().html();
          localStorage.setItem('cooking-list', getcooking);
        });
      })
    },
    listcheck: function (options) {
      var defaults = {
        selector: '.shopping-list li'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var shopobj = jQuery(this).closest('ul');
        shopobj.on( "click", "li", function() {
          jQuery(this).toggleClass("delme");
          var getshopping = jQuery(this).parent().html();
          localStorage.setItem('shopping-list', getshopping);
        });
      })
    },
    shopping: function (options) {
      var defaults = {
        selector: '.shop'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var shopobj = jQuery(this);
        shopobj.click(function(event){

        });
      })
    },
    simpletabs: function (options) {
      var defaults = {
        selector: '.simpletab'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var tabobj = jQuery(this);
        var doSimpletab = "0";
        if (localStorage.getItem('simpletabnumber')) {
          doSimpletab = localStorage.getItem('simpletabnumber');
        }
        jQuery('.simpletabs li').eq(doSimpletab).addClass('selected');
        jQuery('.simpletab-wrapper > div').eq(doSimpletab).show();
        var clicker = jQuery('.simpletabs li');

        clicker.click(function(event){
          jQuery('.simpletabs li').removeClass("selected");
          jQuery(this).addClass("selected");
          var triggerID = jQuery('.simpletabs').find('li').index(this);
          localStorage.setItem('simpletabnumber', triggerID);
          jQuery('.panel').hide();
          jQuery('.simpletab-wrapper > div').eq(triggerID).show();
          event.preventDefault(event);
        });
      })
    },
    saveinfo: function (options) {
      var defaults = {
        selector: '.saver',
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var obj = jQuery(this);
        var getTheId = obj.attr('id');
        jQuery( document ).on( "blur", "#" + getTheId, function() {
          localStorage.setItem(getTheId, this.innerHTML);
          if (getTheId == "ingredients-list") {
            localStorage.setItem('shopping-list', this.innerHTML);
            jQuery('.shopping-list').html(this.innerHTML);
          }
          if (getTheId == "method-list") {
            localStorage.setItem('cooking-list', this.innerHTML);
            jQuery('.cooking-list').html(this.innerHTML);
          }
        });
      })
    },
    getinfo: function (options) {
      var defaults = {
        selector: '.saver',
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var obj = jQuery(this);
        var getTheId = obj.attr('id');
        if (localStorage.getItem(String(getTheId))) {
          obj.html(localStorage.getItem(getTheId));
        }
      })
    },

  }
})(jQuery);

jQuery(function(){	
  jQuery.mark.makecookinglist();
  jQuery.mark.makeshoppinglist();
  jQuery.mark.cookcheck();
  jQuery.mark.listcheck();
  jQuery.mark.shopping();
  jQuery.mark.simpletabs();
  jQuery.mark.saveinfo();
  jQuery.mark.getinfo();
});