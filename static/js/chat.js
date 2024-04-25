function scrollToEnd() {
  const chatMessages = document.querySelector(".chat-messages");
  const lastMessage = chatMessages.lastElementChild;
  if (lastMessage) {
    lastMessage.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
}

function appendRelatedQuestions(questions) {
  const chatbox = document.getElementById("chatbox");

  // Create buttons for each related question
  questions.forEach((question) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "btn btn-light m-1";
    button.textContent = question;
    button.onclick = () => getBotResponse(question);
    chatbox.appendChild(button);
  });

  scrollToEnd();
}

function getQuestions() {
  $.get("/get-answer/", { question: null }).done(function (data) {
    appendRelatedQuestions(data);
  });
}

function getBotResponse(value = undefined) {
  var rawText = value || $("#textInput").val();
  //   console.log(rawText);
  var userHtml = '<p class="userText mt-2"><span>' + rawText + "</span></p>";
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document
    .getElementById("userInput")
    .scrollIntoView({ block: "start", behavior: "smooth" });
  $.get("/get-answer/", { question: rawText }).done(function (data) {
    var botHtml = '<p class="botText"><span>' + data.answer + "</span></p>";
    $("#chatbox").append(botHtml);
    if (data.related_questions.length > 0) {
      $("#chatbox").append(
        '<p class=""><span>' + "Related Questions" + "</span></p>'"
      );
      appendRelatedQuestions(data.related_questions);
    } else {
      var startAgainBtn = document.createElement("button");
      startAgainBtn.classList.add("btn", "btn-light");
      startAgainBtn.textContent = "Start Again";
      startAgainBtn.onclick = (ev) => {
        ev.target.remove();
        getQuestions();
      };
      $("#chatbox").append(startAgainBtn);
      scrollToEnd();
    }
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var input = document.getElementById("textInput");
  input.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      getBotResponse();
    }
  });
});
