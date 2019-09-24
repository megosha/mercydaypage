
function fio(id) {
    inp = document.getElementById(id);
    inp.value = inp.value.replace(/[0-9++=~`!@#$%\^&*()_|\/№\;:?<>,."'{}\[\]]/, '');
}

function teln(id) {
    field = document.getElementById(id);
    field.value = field.value.replace(/[^0-9)( +-]+/g, '');
}