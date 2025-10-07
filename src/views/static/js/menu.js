const fadeTime = 300;
const menuMusicElement = $("#menu-music");
const pabloSoundElement = $("#pablo-sound-effect");
const dogNameElement = $("#pablo-name");
const dogBreedElement = $("#pablo-breed");
const gameUUIDElement = $("#game-uuid");
const splashTextElement = $("#splash-text");
const splashTexts = [
    "É do caralho!",
    "O melhor!",
    "Brabo!",
    "Lucas Samuel Santos!",
    "não grita.",
    "Pablo.",
    "Red Pill Based",
    "Eu não lhe tanko",
    "Vapo.",
    "ReCeBa!!!",
    "amém.",
    "Diga não ao XSS!",
    "SQL Injection é paia",
    "DoS + DDoS = perdemo",
    "Dá não, man",
    "S2",
    "Bola vermelha = models"
]

function fadeInElement(element) {
    $(element).fadeIn(fadeTime);
}

function fadeOutElement(element) {
    $(element).fadeOut(fadeTime);
}

function showErrorMessage(errorElement, message) {
    $(errorElement).stop(true, true);
    
    $(errorElement).text(message);
    $(errorElement).fadeIn(fadeTime);

    setTimeout(() => $(errorElement).fadeOut(fadeTime), 5000);
}

$(window).ready(() => {
    const text = splashTexts[Math.floor(Math.random() * splashTexts.length)];
    splashTextElement.text(text);

    menuMusicElement[0].play();
    pabloSoundElement[0].play();
});

// Create new game button
$("#confirm-dog-info-btn").click(() => {
    const dogName = dogNameElement.val();
    const dogBreed = dogBreedElement.val();

    if (!dogName.replaceAll(" ", "")) {
        showErrorMessage("#input-error", "Erro: Cade o nome do seu Pablo.?");
        return;
    }

    if (!dogBreed.replaceAll(" ", "")) {
        showErrorMessage("#input-error", "Erro: Teu Pablo. não tem raça?");
        return;
    }
    
    $.post({
        url: "create_new_game",
        data: JSON.stringify({
            dog_name: dogName,
            dog_breed: dogBreed
        }),
        contentType: "application/json",
        dataType: "json", 
        success: (data) => {
            window.location = data.redirect_url;
        },
        error: (xhr) => {
            showErrorMessage("#input-error", "Erro: " + xhr.responseJSON.error);
        }
    });
});

// Load game button
$("#send-game-uuid-btn").click(() => {
    gameUuid = gameUUIDElement.val();

    if (!gameUuid) {
        showErrorMessage("#game-uuid-input-error", "Cade o identificador?");
        return;
    }
    
    $.get("load_existing_game", { game:  gameUuid})
        .done((data) => {
            window.location = data.redirect_url;
        })
        .fail((xhr) => {
            showErrorMessage("#game-uuid-input-error", xhr.responseJSON.error);
            gameUUIDElement.val("");
        });
});

// Open dialog boxes
$("#how-to-play-btn").click(() => fadeInElement("#how-to-play-dialog"));
$("#about-btn").click(() => fadeInElement("#about-dialog"));
$("#load-game-btn").click(() => {
    fadeInElement("#load-game-dialog");
    gameUUIDElement.val("");
});
$("#new-game-btn").click(() => {
    fadeInElement("#new-game-dialog");
    dogNameElement.val("");
    dogBreedElement.val("");
});

// Closes dialog boxes
$("#close-how-to-play-dialog").click(() => fadeOutElement("#how-to-play-dialog"));
$("#close-about-dialog").click(() => fadeOutElement("#about-dialog"));
$("#close-load-game-dialog").click(() => fadeOutElement("#load-game-dialog"));
$("#close-new-game-dialog").click(() => fadeOutElement("#new-game-dialog"));
