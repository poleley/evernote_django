"use strict";

import { getCookie } from "./cookie.js";

const csrftoken = getCookie('csrftoken');

const rightBlock = document.querySelector('.rightBlock');

const rsplit = (str, sep, maxsplit) => {
  const split = str.split(sep);
  return maxsplit ? [split.slice(0, -maxsplit).join(sep)].concat(split.slice(-maxsplit)) : split;
}

function showNotes(notes) {
    for (let note of notes) {
        let divNote = document.createElement("div");
        divNote.classList.add('divNote');
        rightBlock.insertBefore(divNote, null);

        let noteRow = document.createElement("div");
        noteRow.classList.add('noteRow');
        divNote.insertBefore(noteRow, null);

        let noteTitle = document.createElement("div");
        noteTitle.innerHTML = note.name;
        noteTitle.classList.add('noteTitle');
        noteRow.insertBefore(noteTitle, null);

        let rightCorner = document.createElement("div");
        rightCorner.classList.add('rightCorner');
        noteRow.insertBefore(rightCorner, null);

        let showNoteSpan = document.createElement("span");
        showNoteSpan.classList.add('showNoteSpan');
        rightCorner.insertBefore(showNoteSpan, null);

        let showNote = document.createElement("span");
        showNote.innerHTML = "Детальный просмотр";
        showNote.setAttribute("data-id", note.id);
        showNote.classList.add('showNote');
        showNoteSpan.insertBefore(showNote, null);
        showNote.addEventListener('click', function () {
            detailedView.classList.add('displayFlex');
        });

        let deleteNote1 = document.createElement("div");
        deleteNote1.classList.add('deleteNote1');
        rightCorner.insertBefore(showNoteSpan, null);

        let a = document.createElement("a");
        a.href = "#";
        deleteNote1.insertBefore(a, null);

        let deleteNote = document.createElement("button");
        deleteNote.classList.add('deleteNote');
        deleteNote.setAttribute("data-id", note.id);
        deleteNote1.insertBefore(deleteNote, null);

        let img = new Image();
        img.src = "https://www.svgrepo.com/show/79440/delete-button.svg";
        img.classList.add('deleteNote')
        rightCorner.insertBefore(img, null);
        img.addEventListener('click', function () {
            fetch('/evernote/api/notes/' + img.dataset.id, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            }).then(
                response => {
                    return response.text();
                }
            ).then(
                text => {
                    divNote.remove();
                    detailedView.remove();
                }
            );
        });


        let noteBody = document.createElement("div");
        noteBody.classList.add('noteBody');
        if (note.text.length > 500)
            noteBody.innerHTML = note.text.slice(0, 500) + "...";
        else
            noteBody.innerHTML = note.text;
        divNote.insertBefore(noteBody, null);

        if (!(note.file == null)) {
            let isFile = document.createElement("div");
            isFile.classList.add('isFile');
            isFile.innerHTML = "К этой заметке прикреплен файл";
            divNote.insertBefore(isFile, null);
        }

        let noteDate = document.createElement("div");
        noteDate.classList.add('noteDate');
        noteDate.innerHTML = note.date;
        divNote.insertBefore(noteDate, null);

        let noteTags = document.createElement("div");
        noteTags.classList.add('noteTags');
        divNote.insertBefore(noteTags, null);

        for (let tag of note.tags) {
            let noteTag = document.createElement("span");
            noteTag.classList.add('noteTag');
            noteTag.innerHTML = "#" + tag;
            noteTags.insertBefore(noteTag, null);
        }

        let addTag = document.createElement("a");
        a.href = "#";
        // add href
        noteTags.insertBefore(addTag, null);

        let addNewTag = document.createElement("button");
        addNewTag.classList.add('addNewTag');
        addNewTag.innerHTML = "+";
        addTag.insertBefore(addNewTag, null);

        let detailedView = document.createElement("div");
        detailedView.classList.add('detailedView');
        detailedView.setAttribute("data-id", note.id);
        divNote.insertBefore(detailedView, null);

        let detailedDivNote = document.createElement("div");
        detailedDivNote.classList.add('detailedDivNote');
        detailedView.insertBefore(detailedDivNote, null);

        noteRow = document.createElement("div");
        noteRow.classList.add('noteRow');
        detailedDivNote.insertBefore(noteRow, null);

        noteTitle = document.createElement("div");
        noteTitle.innerHTML = note.name;
        noteTitle.classList.add('noteTitle');
        noteRow.insertBefore(noteTitle, null);

        rightCorner = document.createElement("div");
        rightCorner.classList.add('rightCorner');
        noteRow.insertBefore(rightCorner, null);

        deleteNote1 = document.createElement("div");
        deleteNote1.classList.add('deleteNote1');
        rightCorner.insertBefore(deleteNote1, null);

        a = document.createElement("a");
        a.href = "#";
        deleteNote1.insertBefore(a, null);

        img = new Image();
        img.src = "https://www.svgrepo.com/show/79440/delete-button.svg";
        img.classList.add('deleteNote');
        img.setAttribute("data-id", note.id);
        a.insertBefore(img, null);
        img.addEventListener('click', function () {
            fetch('/evernote/api/notes/' + img.dataset.id, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            }).then(
                response => {
                    return response.text();
                }
            ).then(
                text => {
                    divNote.remove();
                    detailedView.remove();
                }
            );
        });

        img = new Image();
        img.src = "http://cdn.onlinewebfonts.com/svg/img_251634.png";
        img.setAttribute("data-id", note.id);
        img.classList.add('close');
        deleteNote1.insertBefore(img, null);
        img.addEventListener('click', function () {
            detailedView.classList.remove('displayFlex');
        })

        noteBody = document.createElement("div");
        noteBody.classList.add('noteBody');
        noteBody.innerHTML = note.text;
        detailedDivNote.insertBefore(noteBody, null);

        if (!(note.file == null)) {
            let isFile = document.createElement("div");
            isFile.classList.add('isFile');
            // let downloadFile = document.createElement("a");
            // добавить а href = download file page
            isFile.innerHTML = "Скачать файл " + rsplit(String(note.file), '/', 1)[1];
            detailedDivNote.insertBefore(isFile, null);
            isFile.addEventListener('click', function () {
                window.location.href = `/evernote/download-file/${note.id}`;
                // fetch(`/evernote/download-file/${note.id}`).then(
                //     response => {
                //         return response.text();
                //     });
            });
        }

        noteDate = document.createElement("div");
        noteDate.classList.add('noteDate');
        noteDate.innerHTML = note.date;
        detailedDivNote.insertBefore(noteDate, null);

        noteTags = document.createElement("div");
        noteTags.classList.add('noteTags');
        detailedDivNote.insertBefore(noteTags, null);

        for (let tag of note.tags) {
            let noteTag = document.createElement("span");
            noteTag.classList.add('noteTag');
            noteTag.innerHTML = "#" + tag;
            noteTags.insertBefore(noteTag, null);
        }

        addTag = document.createElement("a");
        a.href = "#";
        // add href
        noteTags.insertBefore(addTag, null);

        addNewTag = document.createElement("button");
        addNewTag.classList.add('addNewTag');
        addNewTag.innerHTML = "+";
        addTag.insertBefore(addNewTag, null);
    }
}

const filterDate = document.querySelector('.filterDate');
const filterTag = document.querySelector('.filterTag');
const filterButton = document.querySelector('.filterButton');
let isFiltered = false;


filterButton.addEventListener('click', function () {
        if (filterDate.value !== '' || filterTag.value !== '') {
            let url;
            if (filterTag.value === '') {
                url = `/evernote/api/notes/?date=${filterDate.value}`;
            } else if (filterDate.value === '') {
                url = `/evernote/api/notes/?tags=${filterTag.value}`;
            } else {
                url = `/evernote/api/notes/?date=${filterDate.value}&tags=${filterTag.value}`;
            }
            isFiltered = true;
            rightBlock.innerHTML = '';
            fetch(url, {
                method: 'GET'
            }).then(
                response => {
                    return response.json();
                }
            ).then(
                notes => showNotes(notes)
            );
        }
    }
)
;


if (!isFiltered) {
    fetch('/evernote/api/notes').then(
        response => {
            return response.json();
        }
    ).then(
        notes => showNotes(notes)
    );
}

const showAll = document.querySelector('.allNotes');
showAll.addEventListener('click', function () {
    rightBlock.innerHTML = '';
    filterDate.value = '';
    filterTag.value = '';
    fetch('/evernote/api/notes').then(
        response => {
            return response.json();
        }
    ).then(
        notes => showNotes(notes)
    );
})

let showMenuButton = document.querySelector('.showMenu');
let menu = document.querySelector('.menu');
showMenuButton.addEventListener('click', function () {
    menu.classList.toggle('displayBlock');
});
