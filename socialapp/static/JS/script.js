const addPostBtn = document.getElementById('addPostBtn');
  const postFormFields = document.getElementById('postFormFields');
  const descriptionField = document.getElementById('descriptionField');
  const imageInput = document.getElementById('id_image'); // Django auto-generates id_image

  // Show form when "Add Post" button is clicked
  addPostBtn.addEventListener('click', function () {
    postFormFields.style.display = 'block';
    addPostBtn.style.display = 'none';
  });

  // Show description when image is selected
  imageInput.addEventListener('change', function () {
    if (imageInput.files.length > 0) {
      descriptionField.style.display = 'block';
    }
});