// init_select2.js
function initializeSelect2() {
    $('.js-operating-load-select').select2().on('change.select2', function (e) {
        htmx.trigger(this, 'myEvent');
        console.log('Selected value:', $(this).val());
    });
}