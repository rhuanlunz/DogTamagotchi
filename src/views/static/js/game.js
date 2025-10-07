const gameUUID = new URL(window.location.href).searchParams.get('save');
const apiUrl = (route) => `/api/dog/${route}?save=${gameUUID}`

const actions = ["Brincar", "Alimentar", "Dormir", "Acordar"];
const routes = ["play", "feed", "sleep", "wake_up"];
let actionCounter = 0;

const dogNameElement = $("#dog-name");
const dogBreedElement = $("#dog-breed");
const dogMessageElement = $("#dog-message");
const dogHungryElement = $("#dog-hungry");
const dogFatigueElement = $("#dog-fatigue");
const dogSleepingElement = $("#dog-sleeping");
const dogWarningElement = $("#dog-warning");
const separatorElement = $(".separator");

const buttonsDiv = $("#buttons-div");
const nextActionBtn = $("#next-action-btn");
const previousActionBtn = $("#previous-action-btn");
const actionBtn = $("#action-btn");

const eatSoundEffect = $("#eat-sound-effect");
const nahSoundEffect = $("#nah-sound-effect");
const sleepSoundEffect = $("#sleep-sound-effect");
const yawningSoundEffect = $("#yawning-sound-effect");

function showDogMessage(message) {
    $(dogMessageElement).stop(true, true); // Interrupt any previous animation

    dogMessageElement.text(message);
    $(dogMessageElement).fadeIn(300);
    
    setTimeout(() => $(dogMessageElement).fadeOut(300), 3000);
}

function updateDogStatus(data) {
    dogHungryElement.text(`Fome: ${data.dog_hunger}/6`);
    dogFatigueElement.text(`Cansaço: ${data.dog_fatigue}/5`);

    if (data.dog_warning) {
        dogWarningElement.text(data.dog_warning);
    }
    else {
        dogWarningElement.text("");
    }

    if (data.dog_hunger == 6) {
        dogNameElement.text("☠️");
        dogWarningElement.css("color", "#8A0000");
        buttonsDiv.hide();
        separatorElement.hide();
        dogHungryElement.hide();
        dogFatigueElement.hide();
        dogSleepingElement.hide();
        return;
    }
    else if (data.dog_hunger > 4) {
        dogHungryElement.css("color", "orange");
    } 
    else {
        dogHungryElement.css("color", "white");
    }

    if (data.dog_fatigue > 3) {
        dogFatigueElement.css("color", "orange");
    }
    else {
        dogFatigueElement.css("color", "white");
    }
    
    if (data.dog_is_sleeping) {
        dogSleepingElement.text("Está dormindo.");
        dogSleepingElement.css("color", "#87CEEB");
        sleepSoundEffect[0].loop = true;
        sleepSoundEffect[0].play();
    } 
    else {
        dogSleepingElement.text("Está acordado.");
        dogSleepingElement.css("color", "white");
    }
}

$(document).ready(() => {
    $.get(apiUrl('status'))
        .done((data) => {
            dogNameElement.text(data.dog_name);
            dogBreedElement.text("Raça: " + data.dog_breed);
            updateDogStatus(data);
        });

    actionBtn.text(actions[actionCounter]);
})

nextActionBtn.click(() => {
    actionCounter++;
    if (actionCounter == actions.length) {
        actionCounter = 0;
    }
    actionBtn.text(actions[actionCounter]);
});

previousActionBtn.click(() => {
    actionCounter--;
    if (actionCounter < 0) {
        actionCounter = actions.length - 1;
    }
    actionBtn.text(actions[actionCounter]);
})

actionBtn.click(async () => {
    const route = routes[actionCounter];
    await $.get(apiUrl(route))
        .done((data) => {
            showDogMessage(data.message);
            
            if (route == "feed") {
                eatSoundEffect[0].play();
            }
            else if (route == "wake_up") {
                sleepSoundEffect[0].loop = false;
                sleepSoundEffect[0].pause();
                sleepSoundEffect[0].currentTime = 0;
                yawningSoundEffect[0].play();
            }
            else if (route == "sleep") {
                sleepSoundEffect[0].loop = true;
                sleepSoundEffect[0].play();
            }
        })
        .fail((data) => {
            showDogMessage(data.responseJSON.message);
            
            if (route == "feed") {
                nahSoundEffect[0].play();
            }
        });
    
    await $.get(apiUrl('status'))
        .done((data) => {
            updateDogStatus(data);
        });
});