function openNavigation() {
  document.getElementById("pmySidenav").style.width = "50%";
}

/* Close/hide the sidenav */
function closeNavigation() {
  document.getElementById("pmySidenav").style.width = "0";
}

function openupevents() {
  closeprevents()
  document.getElementById("upevents").style.display = "block";
}

/* Close/hide the sidenav */
function closeupevents() {
  document.getElementById("upevents").style.display = "none";
}
function openprevents() {
  closeupevents()
  document.getElementById("prevents").style.display = "block";
}

/* Close/hide the sidenav */
function closeprevents() {
  document.getElementById("prevents").style.display = "none";
}