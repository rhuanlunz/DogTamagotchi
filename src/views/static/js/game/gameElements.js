const gameUUID = new URL(window.location.href).searchParams.get('save');
const apiUrl = (route) => `/api/dog/${route}?save=${gameUUID}`

// Dog Elements
const dogNameElement = $("#dog-name");
const dogBreedElement = $("#dog-breed");
const dogMessageElement = $("#dog-message");
const dogHungryElement = $("#dog-hungry");
const dogFatigueElement = $("#dog-fatigue");
const dogSleepingElement = $("#dog-sleeping");
const dogWarningElement = $("#dog-warning");

const separatorElement = $(".separator");

// Buttons
const buttonsDiv = $("#buttons-div");
const nextActionBtn = $("#next-action-btn");
const previousActionBtn = $("#previous-action-btn");
const actionBtn = $("#action-btn");

// Sounds
const gameMusic = $("#game-music");
const eatSoundEffect = $("#eat-sound-effect");
const nahSoundEffect = $("#nah-sound-effect");
const sleepSoundEffect = $("#sleep-sound-effect");
const yawningSoundEffect = $("#yawning-sound-effect");