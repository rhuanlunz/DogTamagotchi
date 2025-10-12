$(document).ready(() => {
    $.get(apiUrl('status'))
        .done((data) => {
            dogNameElement.text(data.dog_name);
            dogBreedElement.text("Raça: " + data.dog_breed);
            updateDogStatus(data);
        });

    actionBtn.text(actions[actionCounter]);

    playGameMusic();
})
