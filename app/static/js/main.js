// Your custom JavaScript code goes here

// Example: Log a message to the console
console.log('Main JavaScript file loaded.');

// Example: Toggle a class on an element
document.addEventListener('DOMContentLoaded', function () {
  var toggleButton = document.getElementById('toggleButton');
  var targetElement = document.getElementById('targetElement');

  if (toggleButton && targetElement) {
    toggleButton.addEventListener('click', function () {
      targetElement.classList.toggle('custom-class');
    });
  }
});

// Example: Show and hide elements
function showElement() {
  var element = document.getElementById('elementToShow');
  if (element) {
    element.style.display = 'block';
  }
}

function hideElement() {
  var element = document.getElementById('elementToHide');
  if (element) {
    element.style.display = 'none';
  }
}

// Example: Form validation
function validateForm() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;

  if (username === '' || password === '') {
    alert('Username and password are required!');
    return false;
  }

  return true;
}

// Example: AJAX request using Fetch API
function fetchData() {
  fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(response => response.json())
    .then(data => {
      console.log('Data received:', data);
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
}

// Example: Handling click events with jQuery
$(document).ready(function () {
  $('#jqueryButton').click(function () {
    alert('Button clicked using jQuery!');
  });
});

// Example: Manipulating the DOM with jQuery
$(document).ready(function () {
  $('#appendTextButton').click(function () {
    $('#textContainer').append('<p>New text added!</p>');
  });
});

// Add more JavaScript code as needed
