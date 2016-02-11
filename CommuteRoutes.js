if(sessionStorage.isInOldSchoolMode == "true"){ //sessionStorage saves everything as a string, and this saves me having to JSON stringify and parse
    //Initialize Old School Menu
    
    //Set appropriate style
    document.body.className += "oldSchool";
} else {
    //Set appropriate style
    document.body.className += "newSchool";
}