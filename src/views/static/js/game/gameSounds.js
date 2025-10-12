function playGameMusic() {
    gameMusic[0].play();
}

function playFeedSound() {
    eatSoundEffect[0].play();
}

function playNotHungrySound() {
    nahSoundEffect[0].play();
}

function playWakeUpSound() {
    yawningSoundEffect[0].play();
}

function playSleepSound() {
    sleepSoundEffect[0].loop = true;
    sleepSoundEffect[0].play();
}

function stopSleepSound() {
    sleepSoundEffect[0].loop = false;
    sleepSoundEffect[0].pause();
    sleepSoundEffect[0].currentTime = 0;
}