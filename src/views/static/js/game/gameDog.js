function updateDogStatus(data) {
    dogHungryElement.text(`Fome: ${data.dog_hunger}/6`);
    dogFatigueElement.text(`Cansaço: ${data.dog_fatigue}/5`);

    updateDogWarning(data.dog_warning);

    updateStyleIfDogIsDead(data.dog_hunger);
    
    updateDogHungerStyle(data.dog_hunger);

    updateDogFatigueStyle(data.dog_fatigue)
    
    updateDogSleepingStyle(data.dog_is_sleeping);
}

function updateDogWarning(dog_warning) {
    if (!dog_warning) {
        resetElementValue(dogWarningElement);
        return;
    }
    
    dogWarningElement.text(dog_warning);
}

function updateStyleIfDogIsDead(dog_hunger) {
    if (dog_hunger == 6) {
        dogNameElement.text("☠️");
        dogWarningElement.css("color", "#8A0000");
        buttonsDiv.hide();
        separatorElement.hide();
        dogHungryElement.hide();
        dogFatigueElement.hide();
        dogSleepingElement.hide();
    }
}

function updateDogHungerStyle(dog_hunger) {
    if (dog_hunger > 4) {
        dogHungryElement.css("color", "orange");
        return;
    } 
    
    dogHungryElement.css("color", "white");
}

function updateDogFatigueStyle(dog_fatigue) {
    if (dog_fatigue > 3) {
        dogFatigueElement.css("color", "orange");
        return;
    }
    
    dogFatigueElement.css("color", "white");
}

function updateDogSleepingStyle(dog_is_sleeping) {
    if (dog_is_sleeping) {
        dogSleepingElement.text("Está dormindo.");
        dogSleepingElement.css("color", "#87CEEB");
        playSleepSound();
        return;
    } 
    
    dogSleepingElement.text("Está acordado.");
    dogSleepingElement.css("color", "white");
}