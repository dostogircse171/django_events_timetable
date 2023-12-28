document.addEventListener('DOMContentLoaded', function () {
    function toggleColorFields() {
        const themeColor = document.querySelector('#id_theme_color');
        const colorFields = document.querySelectorAll('.field-primary_color, .field-background_color, .field-text_color');

        if (themeColor.value === 'dj_timetable_custom') {
            colorFields.forEach(field => field.style.display = 'block');
        } else {
            colorFields.forEach(field => field.style.display = 'none');
        }
    }

    const themeColorSelect = document.querySelector('#id_theme_color');
    if (themeColorSelect) {
        themeColorSelect.addEventListener('change', toggleColorFields);
        toggleColorFields();
    }
});