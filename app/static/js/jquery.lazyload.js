(function(e){e.fn.lazyload=function(t){var n={threshold:0,failurelimit:0,event:"scroll",effect:"show",container:window};t&&e.extend(n,t);var r=this;return"scroll"==n.event&&e(n.container).bind("scroll",function(t){var i=0;r.each(function(){if(!e.abovethetop(this,n)&&!e.leftofbegin(this,n))if(!e.belowthefold(this,n)&&!e.rightoffold(this,n))e(this).trigger("appear");else if(i++>n.failurelimit)return!1});var s=e.grep(r,function(e){return!e.loaded});r=e(s)}),this.each(function(){var t=this;undefined==e(t).attr("original")&&e(t).attr("original",e(t).attr("src")),"scroll"!=n.event||undefined==e(t).attr("src")||n.placeholder==e(t).attr("src")||e.abovethetop(t,n)||e.leftofbegin(t,n)||e.belowthefold(t,n)||e.rightoffold(t,n)?(n.placeholder?e(t).attr("src",n.placeholder):e(t).removeAttr("src"),t.loaded=!1):t.loaded=!0,e(t).one("appear",function(){this.loaded||e("<img />").bind("load",function(){e(t).hide().attr("src",e(t).attr("original"))[n.effect](n.effectspeed),t.loaded=!0}).attr("src",e(t).attr("original"))}),"scroll"!=n.event&&e(t).bind(n.event,function(n){t.loaded||e(t).trigger("appear")})}),e(n.container).trigger(n.event),this},e.belowthefold=function(t,n){if(n.container===undefined||n.container===window)var r=e(window).height()+e(window).scrollTop();else var r=e(n.container).offset().top+e(n.container).height();return r<=e(t).offset().top-n.threshold},e.rightoffold=function(t,n){if(n.container===undefined||n.container===window)var r=e(window).width()+e(window).scrollLeft();else var r=e(n.container).offset().left+e(n.container).width();return r<=e(t).offset().left-n.threshold},e.abovethetop=function(t,n){if(n.container===undefined||n.container===window)var r=e(window).scrollTop();else var r=e(n.container).offset().top;return r>=e(t).offset().top+n.threshold+e(t).height()},e.leftofbegin=function(t,n){if(n.container===undefined||n.container===window)var r=e(window).scrollLeft();else var r=e(n.container).offset().left;return r>=e(t).offset().left+n.threshold+e(t).width()},e.extend(e.expr[":"],{"below-the-fold":"$.belowthefold(a, {threshold : 0, container: window})","above-the-fold":"!$.belowthefold(a, {threshold : 0, container: window})","right-of-fold":"$.rightoffold(a, {threshold : 0, container: window})","left-of-fold":"!$.rightoffold(a, {threshold : 0, container: window})"})})(jQuery),$(function(){$("img").lazyload({placeholder:"/images/130621NOp.jpg",effect:"fadeIn"})})