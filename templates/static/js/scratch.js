

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

YUI().use('node', 'cookie', "event-resize", "transition", "event", function(Y) {

core.setupHtmlClass = function() {
	Y.all('html').removeClass('no-js').addClass('yes-js');
}

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

core.setupAccordion = function() {
	Y.all('.row-project li').each(function(node) {
		node.one('h3').append('<span></span>');
		node.one('a').on('click',function(e) {
			e.preventDefault();
			this.toggleClass('active');
			this.next('div').toggleClass('active');
		});
	});
};

core.setupGlobalNavAccordion = function() {
	if(Y.one('#nav-global h2') !== null) {
		Y.one('#nav-global h2').setStyle('cursor', 'pointer').append('<span></span>').on('click',function(e) {
			this.toggleClass('active');
			this.next('div').toggleClass('active');
		});
	}
};

core.setupAdditionalInfo = function() {
	if(Y.one('#additional-info h2 span') === null) {
		Y.one('#additional-info h2').setStyle('cursor', 'pointer').append('<span></span>').on('click',function(e) {
			this.toggleClass('active');
			this.next('div').toggleClass('active');
		});
	}
};

core.mobileNav = function() {
	Y.one('.nav-primary').insert('<a id="menu" class="nav-toggle">☰</a>','before');
	Y.all('.nav-toggle').on('click', function(e) {
		Y.all('header nav ul').toggleClass('active');
		Y.all('.nav-primary').toggleClass('active');
	});
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
	"outputFeed" : function(el) {
		var element = document.getElementById(el);
		return function(result){
			if (!result.error){
				var output = '';
				var thefeeds = result.feed.entries;
				var spinner = document.getElementById('spinner');
				if(spinner !== null){
					spinner.style.display = 'none';
				}
				if(element.className.indexOf('with-total') != -1){
					output += '<li>We currently have '+thefeeds.length+' vacancies';
				}
				console.log(thefeeds);
				for (var i = 0; i < thefeeds.length; i++){
					output += '<li><a href="{0}">{1} &rsaquo;</a></li>'.format(thefeeds[i].link, thefeeds[i].title);
				}
				element.innerHTML = element.innerHTML + output;
				return output;
			}
		}
	},

	"getFeed" : function(url, numItems, el){
		var feedpointer = new google.feeds.Feed(url); //Google Feed API method
		console.log(numItems);
		if(numItems != null){
			feedpointer.setNumEntries(numItems); //Google Feed API method
		}else{
			feedpointer.setNumEntries(250); //Google Feed API method
		}
		feedpointer.load(this.outputFeed(el)); //Google Feed API method
	}
};

core.parallaxBackground = function() {
	var body = Y.one('html');
	if(window.devicePixelRatio < 1.5){
		Y.on('scroll', function(e) {
			body.setStyle('backgroundPosition', 'center ' + -window.scrollY * 0.5 + 'px');
		});
	}
};

core.homeAnimation = function() {
	if(Y.one('body').hasClass('home')){
		var anim = Y.one('.animation');
		if(anim != null) {
			anim.addClass('run');
		}
	}
};

core.svgFallback = function() {
	if (!Modernizr.svg || !Modernizr.backgroundsize) {
	 	Y.all("img[src$='.svg']").each(function(node) {
	 		node.setAttribute("src", node.getAttribute('src').toString().match(/.*\/(.+?)\./)[0]+'png');
	 	});
	}
};


core.setupAccordion();
core.resizeListener();
core.mobileNav();
core.cookiePolicy();
core.setupGlobalNavAccordion();
core.setupHtmlClass();
core.tabbedContent();
core.parallaxBackground();
core.homeAnimation();
core.svgFallback();

});
