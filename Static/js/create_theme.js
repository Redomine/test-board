let themeButton = document.querySelector('.theme_button');
let postForm = document.querySelector('.post-form');


themeButton.onclick = function() {

  console.log(typeof(postForm));
  if (themeButton.textContent === 'Закрыть форму постинга') {
  themeButton.textContent = 'Создать тред'
  postForm.classList.add('hide');} else {
  themeButton.textContent = 'Закрыть форму постинга'
  postForm.classList.remove('hide')}

};
