// download.js
document.addEventListener("DOMContentLoaded", function () {
    const downloadButton = document.getElementById("download-button");
    const videoUrlInput = document.getElementById("video-url");
  
    downloadButton.addEventListener("click", function () {
      const url = videoUrlInput.value.trim();
      if (url) {
        // Trigger the download with the provided URL
        window.location.href = `/download?url=${encodeURIComponent(url)}`;
      }
    });
  });
  