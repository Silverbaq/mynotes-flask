function selectTopic() {
  var e = document.getElementById("topicList");
  var id = e.options[e.selectedIndex].value;
  window.location = './select_subject?id='+id;
}



function selectSubject() {
  var e = document.getElementById("subjectList");
  var id = e.options[e.selectedIndex].value;
  console.log('yep');
  window.location = './selectnote?id='+id;
}

function showNote(id) {
    var json_obj = JSON.parse(Get("./getNote?id="+id));
    var note = json_obj.note[0].value;
    var e = document.getElementById("txtNote");
    e.innerHTML = note;
}

function deleteNote() {
  var e = document.getElementById("noteList");
  var id = e.options[e.selectedIndex].value;
  var subjectId = document.getElementById("subjectId").value;

   window.location = './deleteNote?id='+id+'&subjectId='+subjectId;
}


function Get(yourUrl){
var Httpreq = new XMLHttpRequest(); // a new request
Httpreq.open("GET",yourUrl,false);
Httpreq.send(null);
return Httpreq.responseText;
}
