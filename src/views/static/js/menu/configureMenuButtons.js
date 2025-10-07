function configureOpenDialogButtons() {
    howToPlayBtn.click(() => fadeInElement(howToPlayDialogElement));
    aboutBtn.click(() => fadeInElement(aboutDialogElement));
    
    loadGameBtn.click(() => {
        fadeInElement(loadGameDialogElement);
        resetElementValue(gameUUIDElement);
    });

    newGameBtn.click(() => {
        fadeInElement(newGameDialogElement);
        resetElementValue(dogNameElement);
        resetElementValue(dogBreedElement);
    });
}

function configureCloseDialogButtons() {
    closeHowToPlayBtn.click(() => fadeOutElement("#how-to-play-dialog"));
    closeAboutBtn.click(() => fadeOutElement("#about-dialog"));
    closeLoadGameBtn.click(() => fadeOutElement("#load-game-dialog"));
    closeNewGameBtn.click(() => fadeOutElement("#new-game-dialog"));   
}

function configureCreateNewGameButton() {
    sendDogInfoBtn.click(() => {
        const dogName = dogNameElement.val();
        const dogBreed = dogBreedElement.val();

        if (!dogName.replaceAll(" ", "")) {
            showErrorMessage(inputErrorElement, "Erro: Cade o nome do seu Pablo.?");
            return;
        }

        if (!dogBreed.replaceAll(" ", "")) {
            showErrorMessage(inputErrorElement, "Erro: Teu Pablo. não tem raça?");
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
                showErrorMessage(inputErrorElement, "Erro: " + xhr.responseJSON.error);
            }
        });
    });
}

function configureLoadGameButton() {
    sendGameUUIDBtn.click(() => {
        gameUUID = gameUUIDElement.val();

        if (!gameUUID) {
            showErrorMessage(gameUUIDInputErrorElement, "Cade o identificador?");
            return;
        }
        
        $.get("load_existing_game", { game:  gameUUID})
            .done((data) => {
                window.location = data.redirect_url;
            })
            .fail((xhr) => {
                showErrorMessage(gameUUIDInputErrorElement, xhr.responseJSON.error);
                resetElementValue(gameUUIDElement);
            });
    });
}