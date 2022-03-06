"use strict";

const rightBlock = document.querySelector('.rightBlock');

fetch('/evernote/api/notes').then(
    response => {
        return response.json();
    }
).then(
    notes => {
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
            a.insertBefore(deleteNote, null);

            let img = new Image();
            img.src = "/evernote/img/delete-button.svg";
            deleteNote.insertBefore(img, null);

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

            deleteNote = document.createElement("button");
            deleteNote.classList.add('deleteNote');
            deleteNote.innerHTML = "Удалить";
            deleteNote.setAttribute("data-id", note.id);
            a.insertBefore(deleteNote, null);
            deleteNote.addEventListener('click', function () {
                fetch('/evernote/api/notes/' + deleteNote.dataset.id + '/', {
                    method: 'DELETE',
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
            img.src = "/evernote/img/delete-button.svg";
            deleteNote.insertBefore(img, null);

            img = new Image();
            img.src = "/evernote/img/x-symbol-svgrepo-com.svg";
            img.setAttribute("data-id", note.id);
            img.classList.add('close');
            deleteNote1.insertBefore(img, null);

            let close = document.createElement("span");
            close.innerHTML = "Закрыть";
            close.classList.add('close');
            deleteNote1.insertBefore(close, null);
            close.addEventListener('click', function () {
                detailedView.classList.remove('displayFlex');
            })

            noteBody = document.createElement("div");
            noteBody.classList.add('noteBody');
            noteBody.innerHTML = note.text;
            detailedDivNote.insertBefore(noteBody, null);

            if (!(note.file == null)) {
                let isFile = document.createElement("div");
                isFile.classList.add('isFile');
                // добавить а href = download dile page
                isFile.innerHTML = "Скачать файл " + note.file.filename;
                detailedDivNote.insertBefore(isFile, null);
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
);

let showMenuButton = document.querySelector('.showMenu');
let menu = document.querySelector('.menu');
showMenuButton.addEventListener('click', function () {
    menu.classList.toggle('displayBlock');
});
