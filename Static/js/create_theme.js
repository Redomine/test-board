let themeButton = document.querySelector('.theme_button');
let postForm = document.querySelector('post-form');

themeButton.onclick = function() {
  console.log(typeof(postForm));
  postForm.classList.add('hide');
  if (themeButton.textContent === 'Закрыть форму постинга') {
  themeButton.textContent = 'Создать тред'} else {
  themeButton.textContent = 'Закрыть форму постинга'}

};
