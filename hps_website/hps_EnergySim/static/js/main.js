$(document).ready(function() {
    initializeSelect2();
    // Call other initialization functions here if needed
    
});

function toggleActiveNav(element) {
    $(element).addClass('active').siblings().removeClass('active');
}