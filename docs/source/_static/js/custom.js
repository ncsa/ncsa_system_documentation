$( document ).ready(function() {

  // Create link and text for navigation back to the documentation hub home page
  var hub_link = document.createElement("a");
  var hub_text = document.createTextNode("Documentation Hub");
  hub_link.appendChild(hub_text);
  hub_link.setAttribute("href", "https://docs.ncsa.illinois.edu");

  var separator = document.createTextNode(" | ");

  // These items are right-aligned in the RTD theme breadcrumbs
  aside = document.querySelector("body > div > section > div > div > div:nth-child(1) > ul > li.wy-breadcrumbs-aside");

  // Next to the default "Edit on GitHub", add a separator, then the hub link.
  aside.prepend(separator);
  aside.prepend(hub_link);
                    
});
