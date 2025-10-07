const fadeTime = 300;

function fadeInElement(element) {
    $(element).fadeIn(fadeTime);
}

function fadeOutElement(element) {
    $(element).fadeOut(fadeTime);
}

function showErrorMessage(errorElement, message) {
    $(errorElement).fadeIn(fadeTime);
    $(errorElement).text(message);
    setTimeout(() => $(errorElement).fadeOut(fadeTime), 5000);
}

// Create new game button
$("#confirm-dog-info-btn").click(() => {
    const dogName = $("#pablo-name").val();
    const dogBreed = $("#pablo-breed").val();

    if (!dogName.replaceAll(" ", "")) {
        showErrorMessage("#name-input-error", "Cade o nome do seu Pablo.?");
        return;
    }

    if (!dogBreed.replaceAll(" ", "")) {
        showErrorMessage("#breed-input-error", "Teu Pablo. não tem raça?");
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
        error: (xhr, status, error) => {
            console.error("Error: ", status, error, xhr.reponseJSON);
        }
    });
});

// Load game button
$("#send-game-uuid-btn").click(() => {
    gameUuid = $("#game-uuid").val();

    if (!gameUuid) {
        showErrorMessage("#game-uuid-input", "Cade o identificador?");
        return;
    }
    
    $.get("load_existing_game", { game:  gameUuid})
        .done((data) => {
            window.location = data.redirect_url;
        })
        .fail(() => {
            showErrorMessage("#game-uuid-input", "Identificador inválido, burro");
        });
});

// Open dialog boxes
$("#how-to-play-btn").click(() => fadeInElement("#how-to-play-dialog"));
$("#about-btn").click(() => fadeInElement("#about-dialog"));
$("#load-game-btn").click(() => fadeInElement("#load-game-dialog"));
$("#new-game-btn").click(() => fadeInElement("#new-game-dialog"));

// Closes dialog boxes
$("#close-how-to-play-dialog").click(() => fadeOutElement("#how-to-play-dialog"));
$("#close-about-dialog").click(() => fadeOutElement("#about-dialog"));
$("#close-load-game-dialog").click(() => fadeOutElement("#load-game-dialog"));
$("#close-new-game-dialog").click(() => fadeOutElement("#new-game-dialog"));
