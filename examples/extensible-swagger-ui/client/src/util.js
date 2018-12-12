/**
 * Filters an array of objects by a string value accross all properties.
 * https://stackoverflow.com/a/44313087/120783
 *
 * @param {any} array
 * @param {any} string
 */
function filterByValue(array, string) {
    return array.filter(o =>
        Object.keys(o).some(k => String(o[k]).toLowerCase().includes(string.toLowerCase())));
}

export {
    filterByValue
}
