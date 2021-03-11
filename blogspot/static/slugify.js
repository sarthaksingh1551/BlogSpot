const inputTitle = document.querySelector('input[name=title');
const inputSlug = document.querySelector('input[name=slug');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g, '-')         // Replacing '&' with '-and-'
    .replace(/[\s\W-]+/g, '-')  // Replacing spaces, dashes and non word characters with '-'
};

inputTitle.addEventListener('keyup', (e) =>{
    inputSlug.setAttribute('value', slugify(inputTitle.value));
});