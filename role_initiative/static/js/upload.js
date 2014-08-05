function getUUID(){
	return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
		var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
		return v.toString(16);
	});
}

// initialize the resumable file object
var r = new Resumable({
	target: "files/store",
	testChunks: false,
	maxChunkRetries: 3,
	chunkRetryInterval: 1000,
	generateUniqueIdentifier: getUUID,
	chunkSize: CHUNK_SIZE,
})

// update the progress bar
r.on('progress', function(){
	var percent = Math.ceil(this.progress()*100) + "%"
	$('#progress-bar').css('width',percent);
	$('#progress-bar').text(percent)
});

// when a new file is added, list it in the file upload area
r.on('fileAdded', listFiles)

// if there's a problem during the upload (with the file or other)
// just quit and submit the form and the error
r.on('fileError', function(file,message){
	console.log(message)	
	$('#error-message').val(message)
	$('#form').submit();
	r.cancel();
})

r.on('complete', function(){
	// delay so the slow ass progress bar can catch up
	setTimeout(function(){
		$('#form').submit();
	}, 500);
})


function listFiles(){
	var html = ['<ul>']
	for(var i = 0; i < r.files.length; i++){
		html.push("<li><span data-index='" + i + "' class='remove-file glyphicon-remove'></span>" + r.files[i].fileName + "</li>")	
	}
	html.push("</ul>")
	$('#files').html(html.join(""))
}


$(document).ready(function(){
	//initialize these DOM mofo's for the file upload
	r.assignBrowse(document.getElementById("file"))
	//r.assignDrop(document.getElementById("file"))

	// punch it, Chewy.
	$('#submit').on("click", function(e){
		if(r.files.length == 0){
			alert("No files in upload!")	
		} else {
			r.upload();
			$(this).hide();
			$(".progress").show();
		}
	});

})
