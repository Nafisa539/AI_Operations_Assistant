async function sendQuestion() {
 
    let question = document.getElementById("question").value;
 
    if (question == "") {
        return;
    }
 
    let chatBox = document.getElementById("chat-box");
 
    chatBox.innerHTML +=
        "<div class='user'><span>" + question + "</span></div>";
 
    document.getElementById("question").value = "";
 
    let response = await fetch("/chat", {
 
        method: "POST",
 
        headers: {
            "Content-Type": "application/json"
        },
 
        body: JSON.stringify({
            message: question
        })
 
    });
 
    let data = await response.json();
 
    chatBox.innerHTML +=
        "<div class='bot'><span>" + data.response + "</span></div>";
 
    chatBox.scrollTop = chatBox.scrollHeight;
}