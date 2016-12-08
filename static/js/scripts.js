function main() {
  $("#generate").click(function(){
  	var numberOfSentences = $("#numberOfSentences").val();
  	
  	$.get("/generate/" + numberOfSentences, function(response) {
	  $('#sentencesContainer').text(response.data);
	});
  });

  $("#generateATweet").click(function(){
  	$.get("/generateTweet/", function(response) {
	  $('#tweetContainer').text(response.data);
	});
  });

  $("#generateASnark").click(function(){
    $.get("/generateSnark/", function(response) {
    $('#snarkContainer').text(response.data);
  });
  });
  
};
$(main);