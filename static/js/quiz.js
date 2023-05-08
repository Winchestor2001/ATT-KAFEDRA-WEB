const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info_box");
const sec_timer = info_box.querySelector(".sec_timer");
const exit_btn = info_box.querySelector(".buttons .quit");
const continue_btn = info_box.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz_box");
const option_list = document.querySelector(".option_list");
const timeCount = quiz_box.querySelector('.timer .time_sec');
const timeLine = quiz_box.querySelector('header .time_line');
const timeOff = quiz_box.querySelector('header .time_text');
let questions;

start_btn.onclick = () => {
    console.log(questions)
    sec_timer.textContent = `${questions[0].timer} seconds`
  info_box.classList.add("activeInfo");
};

exit_btn.onclick = () => {
  info_box.classList.remove("activeInfo");
};

continue_btn.onclick = () => {
  info_box.classList.remove("activeInfo");
  quiz_box.classList.add("activeQuiz");
  showQuestions(0);
  QuestionCounter(1);
  startTimer(questions[0].timer);
//  startTimerLine(0);
};

let questins_count = 0;
let questin_counter = 1;
let counter;
let counterLine;
let timeValue = 15;
let lineWidth = 0;
let userScore = 0;

const next_btn = quiz_box.querySelector('.next_btn');
const result_box = document.querySelector('.result_box');
const restart_quiz = result_box.querySelector('.buttons .restart');
const quit_quiz = result_box.querySelector('.buttons .quit');

restart_quiz.onclick = () => {
  window.location.reload();
}


next_btn.onclick = () =>{
  if (questins_count < questions.length - 1){
    questins_count++;
    questin_counter++;
    showQuestions(questins_count)
    QuestionCounter(questin_counter);
    clearInterval(counter);
    startTimer(timeValue);
    clearInterval(counterLine);
//    startTimerLine(lineWidth);
    next_btn.style.display = 'none';
    timeOff.textContent = 'Time Left';
  }
  else{
    clearInterval(counter);
    clearInterval(counterLine);
    showResultBox();
  }
}

function showQuestions(index) {
  const question_text = document.querySelector(".quiz_text");
  let question_tag = `<span>${questions[index].id}. ${questions[index].question}</span>`;
  let option_tag = `<div class="option"><span>${questions[index][`option1`]}</span></div>
                    <div class="option"><span>${questions[index][`option2`]}</span></div>
                    <div class="option"><span>${questions[index][`option3`]}</span></div>
                    <div class="option"><span>${questions[index][`option4`]}</span></div>`;
  question_text.innerHTML = question_tag;
  option_list.innerHTML = option_tag;
  const option = option_list.querySelectorAll('.option');
  for (let i = 0; i < option.length; i++) {
    option[i].setAttribute('onclick', 'optionSelected(this);')

  }
}

let tickIcon = '<div class="icon tick"><i class="fa-solid fa-check"></i></div>';
let crossIcon = '<div class="icon cross"><i class="fa-solid fa-xmark"></i></div>';

function optionSelected(answer){
  clearInterval(counter);
  clearInterval(counterLine);
  let userAnswer = answer.textContent;
  let correct_answer = questions[questins_count].answer;
  let allOptions = option_list.children.length;
  if (userAnswer === correct_answer){
    userScore += 1;
    answer.classList.add('correct');
    answer.insertAdjacentHTML('beforeend', tickIcon);
  }
  else{
    answer.classList.add('incorrect');
    answer.insertAdjacentHTML('beforeend', crossIcon);
    for (let i = 0; i < allOptions; i++) {
      if (option_list.children[i].textContent == correct_answer){
        option_list.children[i].setAttribute('class', 'option correct')
        option_list.children[i].insertAdjacentHTML('beforeend', tickIcon);
      }
    }
  }

  for (let i = 0; i < allOptions; i++) {
    option_list.children[i].classList.add('disabled');
  }
  next_btn.style.display = 'block';
}

function showResultBox(){
  info_box.classList.remove("activeInfo");
  quiz_box.classList.remove("activeQuiz");
  result_box.classList.add("activeResult");
  const scoreText = result_box.querySelector('.score_text');
  let scoreTag = `<span>and congrats!, You got <p>${userScore}</p> out of <p>${questions.length}</p></span>`
  scoreText.innerHTML = scoreTag;

}

function startTimer(time){
  counter = setInterval(timer, 1000);
  function timer(){
    timeCount.textContent = time;
    time--;
    if (time < 9) {
      let addZero = timeCount.textContent
      timeCount.textContent = '0' + addZero;
    }
    if (time < 0) {
      clearInterval(counter);
      timeCount.textContent = '00';
      timeOff.textContent = 'Time Off';
      let correct_answer = questions[questins_count].answer;
      let allOptions = option_list.children.length;
      for (let i = 0; i < allOptions; i++) {
        if (option_list.children[i].textContent == correct_answer){
          option_list.children[i].setAttribute('class', 'option correct')
          option_list.children[i].insertAdjacentHTML('beforeend', tickIcon);
        }
      }
      for (let i = 0; i < allOptions; i++) {
        option_list.children[i].classList.add('disabled')
      }
      next_btn.style.display = 'block'
    }
  }
}

//function startTimerLine(time){
//  counterLine = setInterval(timer, 29);
//  function timer(){
//    time += 1;
//    timeLine.style.width = time + 'px';
//    if (time > 549) {
//      clearInterval(counterLine);
//
//    }
//  }
//}

function QuestionCounter(index){
  const bottom_question_counter = quiz_box.querySelector('.total_quiz');
  let totalQuestionsCountTag = `<span><p>${index}</p>of<p>${questions.length}</p>Questions</span>`
  bottom_question_counter.innerHTML = totalQuestionsCountTag;
}


async function QuizApi(){
    let result;
    let request = await fetch('https://attkafedra.pythonanywhere.com/e-darslik/{{ subject.subject_slug }}/quiz_api')
    .then((response) => response.json())
    .then((data) => result =  data);
    return result
}

QuizApi().then((data) => {
    questions = data
    timeValue = questions[0].timer
})
