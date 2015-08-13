

//Provides basic templating for strings: TODO: Find a home for this
String.prototype.format = function() {
  var args = arguments;
  return this.replace(/{(\d+)}/g, function(match, number) {
    return typeof args[number] != 'undefined'
      ? args[number]
      : match
    ;
  });
};

YUI().use('node', 'cookie', 'event-resize', 'transition', 'event', 'jsonp', 'json-parse', 'anim', function(Y) {

  core.setupHtmlClass = function() {
    Y.all('html').removeClass('no-js').addClass('yes-js');
  }

  core.setupAdditionalInfo = function() {
    if(Y.one('#additional-info h2 span') === null) {
      Y.one('#additional-info h2').setStyle('cursor', 'pointer').append('<span></span>').on('click',function(e) {
        this.toggleClass('active');
        this.next('div').toggleClass('active');
      });
    }
  };

  core.cookiePolicy = function() {
    function open() {
      YUI().use('node', function(Y) {
        Y.one('body').prepend('<div class="cookie-policy"><div class="wrapper"><a href="?cp=close" class="link-cta">Close</a><p>We use cookies to improve your experience. By your continued use of this site you accept such use. To change your settings please <a href="/privacy-policy#cookies">see our policy</a>.</p></div></div>');
        Y.one('footer.global .legal').addClass('has-cookie');
        Y.one('.cookie-policy .link-cta').on('click',function(e){
          e.preventDefault();
          close();
        });
      });
    }
    function close() {
      YUI().use('node', function(Y) {
        Y.one('.cookie-policy').setStyle('display','none');
        Y.one('footer.global .legal').removeClass('has-cookie');
        setCookie();
      });
    }
    function setCookie() {
      YUI().use('cookie', function (Y) {
        Y.Cookie.set("_cookies_accepted", "true", { expires: new Date("January 12, 2025") });
      });
    }
    if(Y.Cookie.get("_cookies_accepted") != 'true'){
      open();
    }
  };

  core.tabbedContent = function() {
    Y.all('.tabbed-content .accordion-button').on('click', function(e){
      e.preventDefault();
      e.target.get('parentNode').toggleClass('open');
    });
  };

  core.rssLoader = {
    "outputFeed" : function(el, jobType) {
      var element = document.getElementById(el);
      if (jobType === undefined) {
        jobType = '';
      } else {
        jobType = ' ' + jobType;
      }
      return function(result){
        if (!result.error){
          var output = '';
          var thefeeds = result.feed.entries;
          var spinner = document.getElementById('spinner');
          if(spinner !== null){
            spinner.style.display = 'none';
          }
          if(element.className.indexOf('with-total') != -1){
            output += '<li>We currently have '+thefeeds.length+jobType+' vacancies';
          }
          for (var i = 0; i < thefeeds.length; i++){
            output += '<li><a href="{0}">{1} &rsaquo;</a></li>'.format(thefeeds[i].link, thefeeds[i].title);
          }
          element.innerHTML = element.innerHTML + output;
          return output;
        }
      }
    },

    "getFeed" : function(url, numItems, el, jobType){
      var feedpointer = new google.feeds.Feed(url); //Google Feed API method
      if(numItems != null){
        feedpointer.setNumEntries(numItems); //Google Feed API method
      }else{
        feedpointer.setNumEntries(250); //Google Feed API method
      }
      feedpointer.load(this.outputFeed(el, jobType)); //Google Feed API method
    }
  };

  core.svgFallback = function() {
    if (!Modernizr.svg || !Modernizr.backgroundsize) {
      Y.all("img[src$='.svg']").each(function(node) {
        node.setAttribute("src", node.getAttribute('src').toString().match(/.*\/(.+?)\./)[0]+'png');
      });
    }
  };

  core.renderJSON = function (response, id) {
    if (id == undefined) {
        id = '#dynamic-logos';
    }
    var JSON = response;
    var numberPartners = JSON.length;
    var numberToDisplay = numberPartners < 10 ? numberPartners : 10;

    for (var i = 0; i < numberToDisplay; i++) {
      Y.one(id).append(Y.Node.create('<li><img onload="this.style.opacity=\'1\';" src="'+JSON[i].logo+'" alt="'+JSON[i].name+'"></li>'));
    }
  };

  core.loadPartners = function (params, elementID, feedName) {
    if (typeof feedName === 'undefined') {
      feedName = 'partners';
    }

    var partnersAPI = "http://partners.ubuntu.com/" + feedName + ".json";
    var url = partnersAPI + params + "&callback={callback}";
    var callback = function(response) {
        return core.renderJSON(response, elementID);
    }
    Y.jsonp(url, callback);
  };

  core.sectionTabs = function () {
    if (Y.one('.tabbed-content')) {
      var p = Y.one('.tabbed-menu a.active'),
        s = p.get('href').split('#')[1],
        w = (p.get('clientWidth') / 2) - 7,
        x = (p.get('parentNode').getXY()[0] - p.get('parentNode').get('parentNode').getXY()[0]) + w;
      Y.all('.tabbed-menu a').on('click', function (e) {
        e.preventDefault();
        Y.all('.tabbed-menu a').removeClass('active');
        e.currentTarget.addClass('active');
        Y.all('.tabbed-content').addClass('hide');
        s = e.currentTarget.get('hash');
        Y.one(s).removeClass('hide');
        x = (e.currentTarget.get('parentNode').getXY()[0] - e.currentTarget.get('parentNode').get('parentNode').getXY()[0]) + w;
      });
    }
  };

  core.resizeListener = function() {
    Y.on('windowresize', function(e) {
      core.redrawGlobal();
    });
    core.globalInit();
  };

  core.globalInit= function() {
          if (document.documentElement.clientWidth < 768) {
                  core.globalPrepend = 'div.legal';
                  core.setupGlobalNav();
                  core.setupAdditionalInfo();
                  Y.one('.nav-global-wrapper').insert('<h2>Ubuntu websites</h2>','before');
          } else if (document.documentElement.clientWidth >= 768) {
                  core.globalPrepend = 'body';
                  core.setupGlobalNav();
                  Y.all('#additional-info h2').setStyle('cursor', 'default');
          }
  };

  core.redrawGlobal = function() {
    var globalNav = Y.one("#nav-global");
    if (document.documentElement.clientWidth < 768 && core.globalPrepend != 'div.legal') {
      core.globalPrepend = 'div.legal';
      if (globalNav) {
        globalNav.remove();
        core.setupGlobalNav();
        core.setupAdditionalInfo();
        Y.one('.nav-global-wrapper').insert('<h2>Ubuntu websites</h2>','before');
        Y.one('#nav-global h2').setStyle('cursor', 'pointer').append('<span></span>').on('click',function(e) {
          this.toggleClass('active');
          this.next('div').toggleClass('active');
        });
      }
    } else if (document.documentElement.clientWidth >= 768 && core.globalPrepend != 'body') {
      core.globalPrepend = 'body';
      if (globalNav) {
        globalNav.remove();
        core.setupGlobalNav();
      }
    }
  };


  core.cookiePolicy();
  core.setupHtmlClass();
  core.sectionTabs();
  core.tabbedContent();
  core.svgFallback();
  core.setupGlobalNav();
});
