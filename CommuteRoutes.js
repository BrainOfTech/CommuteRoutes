if(sessionStorage.isInOldSchoolMode == "true"){ //sessionStorage saves everything as a string, and this saves me having to JSON stringify and parse
    //Initialize Old School Menu
    //NOTE: UPDATING HERE DOES NOT UPDATE THE NEW SCHOOL MENU AUTOMATICALLY
    var links = [];
    links.push(["./home.html","About"]);
    links.push(["./Requirements.html", "Project Requirements"]);
    links.push(["./schedule.html","Project Schedule"]);
    links.push(["./activity.html","Activity Log"]);
    links.push(["./team.html", "Team"]);
    links.push(["./index.html","Settings"]);
    
    var teamLinks = [];
    teamLinks.push(["./Steven.html", "Steven"]);
    teamLinks.push(["./Shawn.html", "Shawn"]);
    teamLinks.push(["./Sam.html","(S)am"]);
    
    var menuString = "<ul>";
    for(var i = 0; i < links.length; i++){
        menuString += "<li><a href="+links[i][0]+">"+links[i][1]+"</a></li>";
        if(links[i][0]=="./team.html"){
            menuString += "<ul>";
            for(var j = 0; j < teamLinks.length; j++){
                menuString+="<li><a href="+teamLinks[j][0]+">"+teamLinks[j][1]+"</a></li>";
            }
            menuString += "</ul>";
        }
    }
    menuString += "</ul>";
    var oldInnerHTML = document.body.innerHTML;
    document.body.innerHTML = menuString + oldInnerHTML;
    
    //Set appropriate style
    document.body.className += "oldSchool";
} else {
    //Set appropriate style
    document.body.className += "newSchool";
}