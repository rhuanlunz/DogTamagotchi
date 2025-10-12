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
    closeHowToPlayBtn.click(() => fadeOutElement(howToPlayDialogElement));
    closeAboutBtn.click(() => fadeOutElement(aboutDialogElement));
    closeLoadGameBtn.click(() => fadeOutElement(loadGameDialogElement));
    closeNewGameBtn.click(() => fadeOutElement(newGameDialogElement));   
}

function configureCreateNewGameButton() {
    sendDogInfoBtn.click(() => {
        const dogName = dogNameElement.val();
        const dogBreed = dogBreedElement.val();

        if (!dogName.replaceAll(" ", "")) {
            showMessage(inputErrorElement, "Erro: Cade o nome do seu Pablo.?");
            return;
        }

        if (!dogBreed.replaceAll(" ", "")) {
            showMessage(inputErrorElement, "Erro: Teu Pablo. não tem raça?");
            return;
        }
        
        $.post({
            url: "create_new_game",
            data: JSON.stringify({
                dog_name: dogName,
                dog_breed: dogBreed
            }),
            contentType: "application/json",
            dataType: "json"
        })
        .done((data) => redirectToUrl(data.redirect_url))
        .fail((xhr) => showMessage(inputErrorElement, "Erro: " + xhr.responseJSON.error));
    });
}

function configureLoadGameButton() {
    sendGameUUIDBtn.click(() => {
        const gameUUID = gameUUIDElement.val();

        if (!gameUUID) {
            showMessage(gameUUIDInputErrorElement, "Cade o identificador?");
            return;
        }
        
        $.get("load_existing_game", { game:  gameUUID})
            .done((data) => redirectToUrl(data.redirect_url))
            .fail((xhr) => {
                showMessage(gameUUIDInputErrorElement, xhr.responseJSON.error);
                resetElementValue(gameUUIDElement);
            });
    });
}