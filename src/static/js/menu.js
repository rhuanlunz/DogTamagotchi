const fadeTime = 300;

function fadeInElement(element) {
    $(element).fadeIn(fadeTime);
}

function fadeOutElement(element) {
    $(element).fadeOut(fadeTime);
}

// Create new game button
$("#new-game-btn").click(() => {
    $.get("create_new_game")
        .done((data) => window.location = data.redirect_url);
});

// Load game button
$("#send-game-uuid-btn").click(() => {
    gameUuid = $("#game-uuid").val();
    
    $.get("load_existing_game", { game:  gameUuid})
        .done((data) => {
            window.location = data.redirect_url;
        })
        .fail(() => {
            const inputError = "#input-error";
            fadeInElement(inputError);
            setTimeout(() => fadeOutElement(inputError), 5000);
        });
});

// Open dialog boxes
$("#how-to-play-btn").click(() => fadeInElement("#how-to-play-dialog"));
$("#about-btn").click(() => fadeInElement("#about-dialog"));
$("#load-game-btn").click(() => fadeInElement("#load-game-dialog"));

// Closes dialog boxes
$("#close-how-to-play-dialog").click(() => fadeOutElement("#how-to-play-dialog"));
$("#close-about-dialog").click(() => fadeOutElement("#about-dialog"));
$("#close-load-game-dialog").click(() => fadeOutElement("#load-game-dialog"));
