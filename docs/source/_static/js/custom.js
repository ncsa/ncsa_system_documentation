$( document ).ready(function() {

  // Create link and text for navigation back to the documentation hub home page
  var hub_link = document.createElement("a");
  var hub_text = document.createTextNode("Documentation Home Page");
  hub_link.appendChild(hub_text);
  hub_link.setAttribute("href", "https://docs.ncsa.illinois.edu");

  // Open documentation hub home page in new tab when clicked
  hub_link.setAttribute("target","_blank");

  var separator = document.createTextNode(" | ");

  // These items are right-aligned in the RTD theme breadcrumbs
  aside = document.querySelector("body > div > section > div > div > div:nth-child(1) > ul > li.wy-breadcrumbs-aside");

  // Next to the default "Edit on GitHub", add a separator, then the hub link.
  aside.appendChild(separator);
  aside.appendChild(hub_link);
                    
});
