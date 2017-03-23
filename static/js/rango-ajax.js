$(document).ready(function() {
    // JQuery code to be added in here.
    $('#likes_category').click(function(){
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/rango/like_category/', {category_id: catid}, function(data){
			$('#like_countc').html(data);
			    $('#likes_category').hide();
		});
	});

    $('#likes_page').click(function(){
		var pageid;
		pageid = $(this).attr("data-pageid");
		$.get('/rango/like_page/', {page_id: pageid}, function(data){
			$('#like_countp').html(data);
			    $('#likes_page').hide();
		});
	});

	$('#bid').click(function(){
		var bidvalue, pageid;
		bidvalue = $('#bidinput').val();
		pageid = $(this).attr("data-pageid");
		$.get('/rango/bid_page/', {page_id: pageid, bidvalue: bidvalue}, function(data){
			$('#price_late').html(data["highestprice"]);
			$('#number_late').html(data["number"]);
			    $('#bid').hide();
			    $('#bidinput').hide();
		});
	});

	$('#suggestion_cat').keyup(function(){
	    var query;
	    query = $(this).val();
	    $.get('/rango/suggest_category/', {suggestion: query}, function(data){
	        $('#cats').html(data);
	    });
	});

	$('#suggestion_page').keyup(function(){
	    var query;
	    query = $(this).val();
	    $.get('/rango/suggest_page/', {suggestion: query}, function(data){
	        me.html(data);
	    });
	});

    var deadline = $('#deadline').attr("date");
    deadline = new Date(deadline);
	$('#Countdown').countdown({until: deadline });

    $('.rango-add').click(function(){
	    var catid = $(this).attr("data-catid");
        var url = $(this).attr("data-url");
        var title = $(this).attr("data-title");
        var me = $(this)
	    $.get('/rango/add/', {category_id: catid, url: url, title: title}, function(data){
	                   $('#pages').html(data);
	                   me.hide();
	    });
	});

});