let uploadButton = document.getElementById('upload-btn');
let edgeButton = document.getElementById('edge-btn');
let headerTitle = document.getElementById('header-title');
let originalimage = document.getElementsByClassName('og-image')[0];
let edgeimage = document.getElementsByClassName('edge-image')[0];


uploadButton.onclick = function () {
  let input = document.createElement('input');
  input.type = 'file';
  input.accept = 'image/*';
  input.onchange = function (event) {
    let file = event.target.files[0];
    let reader = new FileReader();

    reader.onload = function (event) {
      let image_path = event.target.result;
      originalimage.src = image_path;
      // Add the imagePath to main.py
      // using an appropriate method (e.g., AJAX request).
      // Send the image data to the server
      fetch('/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ imageData: imageData })
      });
      reader.readAsDataURL(file);
    };
    
    input.click();
  
    headerTitle.classList.remove('edge');
    originalimage.classList.remove('invisible');
  };

}

  edgeButton.onclick = function () {
    headerTitle.classList.add('edge');
    edgeimage.classList.remove('invisible');

  };

