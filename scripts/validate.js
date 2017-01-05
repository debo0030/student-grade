// public function to validate required form fields
function validateForm() {

      var valid = true;

      // display warning message if the first name field is empty.
      if(gradeForm.fName.value === "") {
        var name = document.getElementById('fNameWarning');
        name.innerHTML = "* Please enter your first name *";
        valid = false;
       }

      // display warning message if the last name field is empty.
      if(gradeForm.lName.value === "") {
        document.getElementById('lNameWarning').innerHTML = "* Please enter your last name *";
        valid = false;
      }

      // display warning message if a course not selected.
      if(gradeForm.course.options[gradeForm.course.selectedIndex].text === "Select Course") {
        document.getElementById('courseWarning').innerHTML = "* Please select course *";
        valid = false;
      }

      // display warning message if work type not selected.
      if(gradeForm.workType.options[gradeForm.workType.selectedIndex].text === "Select Work Type") {
        valid = false;
        document.getElementById('typeWarning').innerHTML = "* Please select work type *";
      }

      // display warning message if grade(s) not entered.
      if(gradeForm.enterGrades.value === "") {
        document.getElementById('gradeWarning').innerHTML = "* Please enter valid grade(s). *";
        valid = false;
      }

      return valid; 
};

