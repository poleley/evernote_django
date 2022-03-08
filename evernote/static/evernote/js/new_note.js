"use strict"

import { getCookie } from './cookie.js'

const csrftoken = getCookie('csrftoken');

// const title = document.querySelector('.noteTitle');
// const text = document.querySelector('.noteBody');
// const file = document.querySelector('.file');
// const saveButton = document.querySelector('.save');

const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    fetch('/evernote/api/notes/', {
        method: 'POST',
        headers: {
                    'X-CSRFToken': csrftoken
                },
        body: new FormData(this),
    }).then(
        response => {
            return response.json();
        }
    ).then(
        window.location.replace("/evernote/main")
    )
    event.preventDefault();
});
