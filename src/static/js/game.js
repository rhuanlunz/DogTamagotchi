const gameUUID = new URL(window.location.href).searchParams.get('save');
const apiUrl = (route) => `/api/dog/${route}?save=${gameUUID}`

const dogNameElement = $("#dog-name");
const dogMessageElement = $("#dog-message");

const wakeUpBtn = $("#wake-up-btn");
const sleepBtn = $("#sleep-btn");
const feedBtn = $("#feed-btn");
const playBtn = $("#play-btn");
const showStatusBtn = $("#show-status-btn");

function showDogMessage(message) {
    dogMessageElement.text(message);
    $(dogMessageElement).fadeIn(300);
    
    setTimeout(() => {
        $(dogMessageElement).fadeOut(300);
    }, 3000);    
}

$(document).ready(() => {
    $.get(apiUrl('status'))
        .done((data) => {
            dogNameElement.text(data.dog_name);
        })
})

wakeUpBtn.click(function() {
    $.get(apiUrl("wake_up"))
        .done((data) => {
            showDogMessage(data.message);
        })
        .fail((data) => {
            showDogMessage(data.responseJSON.message);
        })
});

sleepBtn.click(function() {
    $.get(apiUrl("sleep"))
        .done((data) => {
            showDogMessage(data.message);
        })
        .fail((data) => {
            showDogMessage(data.responseJSON.message);
        })
});

feedBtn.click(function() {
    $.get(apiUrl("feed"))
        .done((data) => {
            showDogMessage(data.message);
        })
        .fail((data) => {
            showDogMessage(data.responseJSON.message);
        })
});

playBtn.click(function() {
    $.get(apiUrl("play"))
        .done((data) => {
            showDogMessage(data.message);
        })
        .fail((data) => {
            showDogMessage(data.responseJSON.message);
        })
});

showStatusBtn.click(function() {
});