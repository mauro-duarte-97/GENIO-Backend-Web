// Función para mostrar el recuadro de registro al hacer clic en el botón "O registrate acá"
document.getElementById('toggleButton').addEventListener('click', function() {
  var formContainer = document.getElementById('conteinerRegistro');
  var registerCard = document.getElementById('registerCard');
  var overlay = document.getElementById('overlay');

  formContainer.classList.remove('hidden'); // Eliminar la clase hidden
  registerCard.style.display = 'block'; // Mostrar el cuadro de registro encima
  overlay.style.display = 'block'; // Mostrar el overlay
  document.body.classList.add('blur'); // Aplicar el efecto de blur a los elementos debajo del overlay
  
  // Función para cerrar el panel de registro cuando se hace clic fuera de él
  overlay.addEventListener('click', function() {
    formContainer.classList.add('hidden'); // Ocultar el panel de registro
    overlay.style.display = 'none'; // Ocultar el overlay
    registerCard.style.display = 'none';
    document.body.classList.remove('blur'); // Quitar el efecto de blur
  });
});

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}

function handleCredentialResponse(resp) {
  console.log('resp', resp);
}
  