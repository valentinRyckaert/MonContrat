// copie la valeur dans le presse papier
function copie(value) {
  var tempInput = document.createElement("input"); // récupération du boutton à utiliser
  tempInput.value = value; // ce qui doit être copié est récupéré
  document.body.appendChild(tempInput);
  tempInput.select();
  document.execCommand("copy"); // execution de la commande 'copy'
  document.body.removeChild(tempInput); // suppression de la variable temporaire
}

function afficherValid() {
  // Récupère l'élément du bouton caché
  var boutonCacher = document.getElementById('cacher_valid');

  // Change le style pour l'afficher
  boutonCacher.style.display = 'block';
}