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