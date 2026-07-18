const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
 
sendBtn.addEventListener("click", sendMessage);
 
userInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
 
function addMessage(sender, message) {
 
    const messageDiv = document.createElement("div");
 
    if (sender === "You") {
        messageDiv.className = "user-message";
    } else {
        messageDiv.className = "bot-message";
    }
 
    messageDiv.innerHTML = message.replace(/\n/g, "<br>");
 
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
 
function sendMessage() {
 
    const message = userInput.value.trim();
 
    if (message === "") {
        return;
    }
 
    addMessage("You", message);
 
    userInput.value = "";
 
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        addMessage("Bot", data.response);
    })
    .catch(error => {
        addMessage("Bot", "Error connecting to the server.");
        console.error(error);
    });
}