// init_select2.js
function initializeSelect2() {
    console.log('initializeSelect2 function called');

    $('.js-operating-load-select').each(function() {
        $(this).prop('disabled', false);
    }).select2({
        width: '100%'
    }).on('change.select2', function (e) {
        htmx.trigger(this, 'select2Change');
        console.log('Selected value:', $(this).val());
    });
}
