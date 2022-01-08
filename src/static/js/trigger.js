const options = {
    bottom: '32px', // default: '32px'
    right: '32px', // default: '32px'
    left: 'unset', // default: 'unset'
    time: '0.5s', // default: '0.3s'
    mixColor: '#fff', // default: '#fff'
    backgroundColor: '#ffffff',  // default: '#fff'
    buttonColorDark: '#443B2F',  // default: '#100f2c'
    buttonColorLight: '#ffffff', // default: '#fff'
    saveInCookies: true, // default: true,
    label: '🌙 ', // default: ''
    autoMatchOsTheme: true // default: true
}
// darkmode trigger
const darkmode = new Darkmode(options);
darkmode.showWidget();
// sidenav trigger
$(document).ready(function () {
    $('.sidenav').sidenav();
});
// collapsible trigger
$(document).ready(function () {
    $('.collapsible').collapsible();
});