const splashTexts = [
    "É do caralho!",
    "O melhor!",
    "Brabo!",
    "Lucas Samuel Santos!",
    "não grita.",
    "Pablo.",
    "Red Pill Based",
    "Eu não lhe tanko",
    "Vapo.",
    "Receba!!!",
    "amém.",
    "Diga não ao XSS!",
    "SQL Injection é paia",
    "DoS + DDoS = perdemo",
    "Dá não, man",
    "S2",
    "Bola vermelha = models",
    "Alimente o Pablo.",
    "mvc é vida!!!!!!",
    "clean arch na calculadora!",
    "vai corinthians!",
    "LHP"
]

$(window).ready(() => {
    const text = splashTexts[Math.floor(Math.random() * splashTexts.length)];
    splashTextElement.text(text);

    playMenuMusic();
    playPabloSound();
});

configureCreateNewGameButton();

configureLoadGameButton();

configureOpenDialogButtons();

configureCloseDialogButtons();