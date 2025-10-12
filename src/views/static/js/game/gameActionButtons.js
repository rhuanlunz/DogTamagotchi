const actions = ["Brincar", "Alimentar", "Dormir", "Acordar"];
const routes = ["play", "feed", "sleep", "wake_up"];
let actionCounter = 0;

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
            showMessage(dogMessageElement, data.message);
            
            if (route == "feed") {
                playFeedSound();
            }
            else if (route == "wake_up") {
                stopSleepSound();
                playWakeUpSound();
            }
            else if (route == "sleep") {
                playSleepSound();
            }
        })
        .fail((data) => {
            showMessage(dogMessageElement, data.responseJSON.message);
            
            if (route == "feed") {
                playNotHungrySound();
            }
        });
    
    await $.get(apiUrl('status'))
        .done((data) => updateDogStatus(data));
});

