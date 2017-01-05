//  clear the warning message when the firstName is entered
document.getElementById('fName').addEventListener("blur", function() {
  if(this.value !== "") {
    fNameWarning.innerHTML = "";
  }
});
 
// clear the warning message when the lastName is entered
document.getElementById('lName').addEventListener("blur", function() {
  if(this.value !== "") {
    lNameWarning.innerHTML = "";
  }
});

// clear the warning message when the course is selected
document.getElementById("course").addEventListener("blur", function() {
  if(gradeForm.course.options[gradeForm.course.selectedIndex].text !== "Select Course") {
  courseWarning.innerHTML = "";
  }
});

// clear the warning message when the country is selected
document.getElementById('workType').addEventListener("blur", function() {
  if(gradeForm.workType.options[gradeForm.workType.selectedIndex].text !== "Select Work Type") {
    typeWarning.innerHTML = "";
  }
});

// clear the warning message when grades are entered
document.getElementById('enterGrades').addEventListener("blur", function() {
  if(this.value !== "") {
    gradeWarning.innerHTML = "";
  }
});

document.gradeForm.addEventListener("submit", validateForm);
