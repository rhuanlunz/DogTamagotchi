const fadeTime = 300;

function fadeInElement(element) {
    element.fadeIn(fadeTime);
}

function fadeOutElement(element) {
    element.fadeOut(fadeTime);
}

function resetElementValue(element) {
    element.val("");
}

function showErrorMessage(errorElement, message) {
    errorElement.stop(true, true);
    
    errorElement.text(message);
    errorElement.fadeIn(fadeTime);

    setTimeout(() => errorElement.fadeOut(fadeTime), 5000);
}