$( document ).ready(function() {

  // Create link and text for navigation back to the documentation hub home page
  var hub_link = document.createElement("a");
  var hub_text = document.createTextNode("Documentation Home Page");
  olcf_link.appendChild(hub_text);
  olcf_link.setAttribute("href", "https://docs.ncsa.illinois.edu");

  // Open documentation hub home page in new tab when clicked
  hub_link.setAttribute("target","_blank");

  var separator = document.createTextNode(" | ");


                    
});
