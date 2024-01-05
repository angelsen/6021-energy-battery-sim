// init_select2.js
function initializeSelect2() {
    $('.js-example-basic-single').select2().on('change.select2', function (e) {
        // Code to execute when an option is selected or removed in Select2
        // This function is called whenever the 'change' event occurs on the Select2 element
        htmx.trigger(this, 'myEvent');
        // Example action: Logging the selected value
        console.log('Selected value:', $(this).val());
    });
}