<!--
$(document).ready(function() {
	
	$("#signInButton").click(function() {
		$("#logIn").show('slow');
	});

	$('#header').mouseenter(function() {
		$("#logIn").css({'opacity' : '1'});
	});
	$('#header').mouseleave(function() {
		$("#logIn").hide('slow');
		$("#logIn").css({'opacity' : '0.6'});
	});

	$("#signInButton").click(function() {
		$("#logIn").show('slow');
	});

	$("#logIn").hide();
	$('#loginButton').mouseenter(function() {
		$(this).width(29);
		$(this).height(29);
	});
	$('#loginButton').mouseleave(function() {
		$(this).width(24);
		$(this).height(24);
	});
	
	$(".addMenuCell").hide();
	
	$("#showMail").click(function() {
		$("#addMail").toggle('slow');
	});
	
	$("#showMessenger").click(function() {
		$("#addMessenger").toggle('slow');
	});
	
	$("#showTwitter").click(function() {
		$("#addTwitter").toggle('slow');
	});
	
	$("#showRss").click(function() {
		$("#addRss").toggle('slow');
	});
	
	$('.registration .rounded-corners').mouseover(function() {
		$(this).css({'background-color' : '#FFF'});
	});
	$('.registration .rounded-corners').mouseout(function() {
		$(this).css({'background-color' : '#EEEFFF'});
	});
	
	$('#userdata .rounded-corners').mouseover(function() {
		$(this).css({'background-color' : '#FFF'});
	});
	$('#userdata .rounded-corners').mouseout(function() {
		$(this).css({'background-color' : '#EEEFFF'});
	});
});
//-->