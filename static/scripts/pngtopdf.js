const form = document.querySelector('#upload-form');
const input = document.querySelector('#image-input');
const btn = document.querySelector('#convert-btn');
const error = document.querySelector('#error-message');
const resultLink = document.querySelector('#result-link');
const preview = document.querySelector('#image-preview');



form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Check if an image is selected
  if (!input.files || !input.files[0]) {
    error.textContent = "Please select an image.";
    return;
  }

  const file = input.files[0];

  // Check if the selected file is a PNG image
  if (file.type !== 'image/png') {
    error.textContent = "The selected file is not a PNG image.";
    return;
  }

  // Check if the selected file is less than 10MB
  if (file.size > 10 * 1024 * 1024) {
    error.textContent = "The selected image exceeds the maximum size limit of 10 MB.";
    return;
  }

  // Prepare the form data and send a POST request to the server
  const formData = new FormData();
  formData.append('image', file);

  fetch('/api/pngtopdf', {
    method: 'POST',
    body: formData
  })
  .then(response => response.blob())
  .then(blob => {
    // Create a blob URL for the converted PDF document
    const url = URL.createObjectURL(blob);

    // Display a download link for the result PDF document
    resultLink.innerHTML = `<a href="${url}" download="converted.pdf">Download Converted PDF</a>`;
  })
  .catch(error => console.error(error));
});


input.addEventListener('change', () => {
  // Check if an image is selected
  if (!input.files || !input.files[0]) {
  return;
  }
  
  const reader = new FileReader();
  reader.onload = (event) => {
  // Create an IMG element with the preview image
  const img = document.createElement('img');
  img.src = event.target.result;
  
  // Append the IMG element to the preview container
  preview.innerHTML = '';
  preview.appendChild(img);
  };
  reader.readAsDataURL(input.files[0]);
  });