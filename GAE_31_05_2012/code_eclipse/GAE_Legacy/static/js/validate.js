<!--
var numericExpression = /^[0-9]+$/;
var characterExpression = /^[a-zA-Z]+$/;
var errormsg = "";

var validUsername = false;
function username_validate() {
	validUsername = true;
	var i = 0;
	var input = document.getElementById("username").value.toString();
	if(input.length<6) {
		errormsg = "Username must be at least 6 characters long.";
		validUsername = false;
	} else {
		if(!input.charAt(0).match(characterExpression)) {
			validUsername = false;
			errormsg = "The username must start with a letter (a-zA-Z)";
		} else {
			while(i<input.length && validUsername) {
				if (!input.charAt(i).match(characterExpression) && !input.charAt(i).match(numericExpression)) {
					validUsername = false;
					errormsg = "This username contains invalid characters.";
				}
				i++;
			}
		}
	}
	if (validUsername)
		check_availability(input);
		alert(input+" : "+errormsg);
	errorCheck(validUsername,true,"errorUsername",errormsg,"usernameLabel","username");
}

var validPassword = false;
function password_validate() {
	validPassword = true;
	var i = 0;
	var unsafe = true;
	var unsafe2 = true;
	var input = document.getElementById("pswd").value.toString();
	if(input.length<6 && validPassword) {
		errormsg = "Password must be at least 6 characters long.";
		validPassword = false;
	} else {
		while(i<input.length && validPassword) {
			if (!input.charAt(i).match(characterExpression) && !input.charAt(i).match(numericExpression)) {
				validPassword=false;
				errormsg="This password contains invalid characters.";
			}
			i++;
		}
	}
	if(validPassword) {
		i=0;
		while(i<input.length) {
			if (input.charAt(i).match(characterExpression))
				unsafe=false;
			i++;
		}
		i=0;
		while(i<input.length) {
			if (input.charAt(i).match(numericExpression))
				unsafe2=false;
			i++;
		}
		if(unsafe || unsafe2) {
			validPassword=false;
	    	errormsg="The password must contain alphabetic (A-Z or a-z) and numeric (0-9) characters.";
		}
	}
	errorCheck(validPassword,true,"errorPassword",errormsg,"passwordLabel","pswd");
	if(input!=document.getElementById("re-pswd").value.toString() && validPassword) {
    	validPassword=false;
    	errormsg="Passwords do not match";
	}
	errorCheck(validPassword,true,"errorPassword",errormsg,"passwordLabel","re-pswd");
}

var validEmail = false;
var legalEmailExpression = /^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$/;
function email_validate() {
	validEmail=true;
	var i=0;
	var invalid=0;
	var input = document.getElementById("e-mail").value.toString();
	if (!input.match(legalEmailExpression)) {
		validEmail=false;
		errormsg="This E-mail is invalid.";
	}
	errorCheck(validEmail,true,"errorEmail",errormsg,"emailLabel","e-mail");
}

var validAnswer = false;
function answer_validate() {
	validAnswer=true;
	var i=0;
	var input = document.getElementById("answer").value.toString();
	if(document.getElementById("secretQuestion").value=="") {
		validAnswer=false;
		errormsg="Please select a question first.";
		document.getElementById("secretQuestion").style.borderColor="#ff0000";
	}
	else {
		document.getElementById("secretQuestion").style.borderColor=null;
	}
	while(i<input.length && validAnswer) {
	    if (!input.charAt(i).match(characterExpression) && !input.charAt(i).match(numericExpression)) {
	    	validAnswer=false;
	    	errormsg="This answer contains invalid characters.";
	    }
	    i++;
	}
	if(input=="") {
		validAnswer=false;
		errormsg="Please answer your question.";
		document.getElementById("secretQuestion").style.borderColor="#ff0000";
	}
	errorCheck(validAnswer,true,"errorAnswer",errormsg,"answerLabel","answer");
}

var validName = true;
function name_validate() {
	validName=true;
	var i=0;
	var input = document.getElementById("name").value.toString();
	while(i<input.length && validName) {
	    if (!input.charAt(i).match(characterExpression) && !input.charAt(i).match(numericExpression)) {
	    	validName=false;
	    	errormsg="Your name contains invalid characters.";
	    }
	    i++;
	}
	if(input=="" && document.getElementById("name").value=="") {
		validLastname=true;
		validName=true;
	}
	errorCheck(validName,validLastname,"errorName",errormsg,"nameLabel","name");
	if (validName)
		document.getElementById("name").style.borderColor=null;
}

var validLastname = true;
function lastname_validate() {
	validLastname=true;
	var i=0;
	var input = document.getElementById("lastname").value.toString();
	while(i<input.length && validLastname) {
	    if (!input.charAt(i).match(characterExpression) && !input.charAt(i).match(numericExpression)) {
	    	validLastname=false;
	    	errormsg="Your name contains invalid characters.";
	    }
	    i++;
	}
	if(input=="" && document.getElementById("name").value=="") {
		validLastname=true;
		validName=true;
	}
	errorCheck(validName,validLastname,"errorName",errormsg,"nameLabel","lastname");
	if (validLastname)
		document.getElementById("lastname").style.borderColor=null;
}

var validDate = true;
function date_validate() {
	validDate=true;
	var i=0;
	if(document.getElementById("bDay").value=="" && document.getElementById("bMonth").value=="" && document.getElementById("bYear").value=="")
		validDate=true;
	else
		if(document.getElementById("bDay").value=="" || document.getElementById("bMonth").value=="" || document.getElementById("bYear").value=="") {
			validDate=false;
			errormsg="You forgot some date fields empty";
		}
		else {
			var day=parseInt(document.getElementById("bDay").value);
			var month=parseInt(document.getElementById("bMonth").value);
			var year=parseInt(document.getElementById("bYear").value);
			if((month==4 ||month==6 ||month==9 ||month==11) && (day>30)) {
				validDate=false;
				errormsg="This date is incorrect";
			}
			if(month==2)
				if (day>29) {
					validDate=false;
					errormsg="This date is incorrect";
				}
				else
					if(day==29)
						if(!( !((year) % 4) && ( (year) % 100 || !((year) % 400) ) )) {
							validDate=false;
							errormsg="This date is incorrect";
						}
		}
	if (!validDate) {
		document.getElementById("errorDate").innerHTML =errormsg;
		document.getElementById("dateLabel").style.color="#ff0000";
		document.getElementById("submitRegistration").disabled=true;
		document.getElementById("submitRegistration").style.cursor="not-allowed";
	} else {
		document.getElementById("errorDate").innerHTML ="";
		document.getElementById("dateLabel").style.color="#BBB";
		document.getElementById("submitRegistration").disabled=false;
		document.getElementById("submitRegistration").style.cursor="default";
	}
}

var validWeb = true;
var legalWebExpression = /^[(/\.a-zA-Z0-9-_)+]$/;
function website_validate() {
	validWeb = true;
	var i = 0;
	var input = document.getElementById("website").value.toString();
	while(i<input.length) {
	    if (!input.charAt(i).match(legalWebExpression)) {
	    	validWeb = false;
	    	errormsg = "This is an invalid web address";
	    }
	    i++;
	}
	errorCheck(validWeb,true,"errorWebsite",errormsg,"websiteLabel","website");
}

function errorCheck(valid1,valid2,errorfld,errormsg,label,field) {

	if (!valid1 || !valid2) {
		document.getElementById(errorfld).innerHTML =errormsg;
		document.getElementById(label).style.color="#ff0000";
		document.getElementById(field).style.borderColor="#ff0000";
		document.getElementById("submitRegistration").disabled=true;
		document.getElementById("submitRegistration").style.cursor="not-allowed";
	} else {
		document.getElementById(errorfld).innerHTML ="";
		document.getElementById(label).style.color="#BBB";
		document.getElementById(field).style.borderColor=null;
		document.getElementById("submitRegistration").disabled=false;
		document.getElementById("submitRegistration").style.cursor="default";
	}
}
function disable() {
	if(!validUsername || !validPassword|| !validEmail|| !validAnswer || !validName || !validLastname || !validDate || !validWeb) {
		document.getElementById("submitRegistration").style.cursor="not-allowed";
		document.getElementById("submitRegistration").disabled=true;
	}
}

function check_availability(username){ 
    //use ajax to run the check  
    result = $.post("/check", { username: username },  
        function(result){
    		alert(result);
            if(result == 2)  
            	errormsg = username + ' is not Available' + result;
            	validUsername = false;
           });
}
//-->