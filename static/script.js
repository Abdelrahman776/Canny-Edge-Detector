let uploadButton = document.getElementById('upload-btn');
let edgeButton = document.getElementById('edge-btn');
let headerTitle = document.getElementById('header-title');
let originalimage = document.getElementById('og-image');
let edgeimage = document.getElementById('edge-image');
let imageInput = document.getElementById('img-input');






uploadButton.onclick = function () {
  // imageInput.click();
  headerTitle.classList.remove('edge');
  originalimage.classList.remove('invisible');
  edgeimage.classList.add('invisible');
};






edgeButton.onclick = function () {
  headerTitle.classList.add('edge');
  edgeimage.classList.remove('invisible');
};

