document.addEventListener("DOMContentLoaded", () => {
    let sendBtn = document.getElementById("send-btn"),
        voiceBtn = document.getElementById("voice-btn"),
        chatInput = document.getElementById("chat-input"),
        chatBox = document.getElementById("chat-box"),
        themeBtn = document.querySelector(".theme-btn"),
        isDarkMode = true;

    themeBtn.addEventListener("click", () => {
        document.body.style.background = isDarkMode ? "#ffffff" : "#0d0d0d";
        document.body.style.color = isDarkMode ? "#000000" : "#ffffff";
        document.querySelector(".sidebar").style.background = isDarkMode ? "#f0f0f0" : "#1e1e1e";
        document.querySelector(".chat-container").style.background = isDarkMode ? "#e6e6e6" : "#121212";
        document.querySelector(".chat-input").style.background = isDarkMode ? "#d9d9d9" : "#292929";
        chatInput.style.color = isDarkMode ? "#000000" : "#ffffff";
        
        document.querySelectorAll(".bot-message").forEach(msg => {
            msg.style.background = isDarkMode ? "#00FFFF" : "#292929";
        });
        
        themeBtn.textContent = isDarkMode ? "Dark Mode" : "Light Mode";
        isDarkMode = !isDarkMode;
    });

    if (!sendBtn || !voiceBtn || !chatInput || !chatBox) {
        console.error("One or more elements not found! Check your HTML.");
        return;
    }

    sendBtn.addEventListener("click", sendMessage);
    voiceBtn.addEventListener("click", startVoiceRecognition);
    chatInput.addEventListener("keydown", event => { if (event.key === "Enter") sendMessage(); });

    function sendMessage() {
        let messageText = chatInput.value.trim();
        if (!messageText) return;
        chatBox.appendChild(createMessageElement(messageText, "user-message"));
        let typingMessage = createTypingAnimation();
        chatBox.appendChild(typingMessage);
        chatBox.scrollTop = chatBox.scrollHeight;

        fetch("http://127.0.0.1:5000/chat", {
            method: "POST", headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: messageText })
        })
        .then(response => response.json())
        .then(data => {
            chatBox.removeChild(typingMessage);
            let botMsg = createMessageElement(data.response, "bot-message");
            botMsg.style.background = isDarkMode ? "#292929" : "#00FFFF";
            chatBox.appendChild(botMsg);
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => {
            console.error("Fetch error:", error);
            chatBox.removeChild(typingMessage);
            let errorMsg = createMessageElement("Oops! Something went wrong.", "bot-message");
            errorMsg.style.background = isDarkMode ? "#292929" : "#00FFFF";
            chatBox.appendChild(errorMsg);
        });
        chatInput.value = "";
    }

    function createMessageElement(text, className) {
        let messageElement = document.createElement("div");
        messageElement.classList.add("message", className);
        messageElement.innerHTML = text;
        return messageElement;
    }

    function createTypingAnimation() {
        let typingElement = document.createElement("div");
        typingElement.classList.add("typing-animation", "bot-message");
        typingElement.innerHTML = '<span></span><span></span><span></span>';
        return typingElement;
    }

    function startVoiceRecognition() {
        if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
            alert("Your browser does not support Speech Recognition");
            return;
        }
    
        let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.continuous = false; 
    
        recognition.onstart = () => {
            console.log("Voice recognition started...");
            voiceBtn.style.background = "red";
        };
    
        recognition.onresult = event => {
            console.log("Voice input received:", event.results[0][0].transcript);
            chatInput.value = event.results[0][0].transcript;
        };
    
        recognition.onerror = event => {
            console.error("Speech recognition error:", event.error);
            alert("Error: " + event.error);
        };
    
        recognition.onend = () => {
            console.log("Voice recognition ended.");
            voiceBtn.style.background = "cyan";
        };
    
        recognition.start();
    }
    
});